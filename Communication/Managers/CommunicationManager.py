import sys
import errno
import threading
import time
from Communication.Include.Comm import Subscriber, Publisher
from Modules.GenericProtoManager import GenericProtoManager, Configuration, PROJECT_ROOT, logger, ChainResponsibility, Util
import queue
import os
from datetime import datetime
import csv

"""Liad Kashanovsky - Communication Manager, ZMQ Sub/Pub topic filtered Protobuf message
1. Register Protobuf Callback function
2. Call registered callback when Protobuf arrived.
3. Protopuf arrives via ZMQ Subscriber/Publisher communication
4. Protobuf message is subscribed to listen to Publisher via config.server_ip:config:port
__________________________________________________________________________________________________________
"""

"""
1. Connect to Publisher
2. Wait for Publisher topic
3. Wait for Protobuf message
4. Call to registered Protobuf callback as defined in config.message per Protobuff topic if defined specific one or general if not
5. Protobuf message can be subscribed to Publisher address per Protobuf topic using config.messages or use general config.server_ip:config.server_port"""
def wait_for_proto_message(self, oServer, oServerTopic, sChainRespCallback, sChainRespCallbackFailure):
    logger.info("Start wait_for_proto_message")
    time.sleep(1)
    ip = oServer["ip"]
    port = oServer["port"]

    if self.oConfig.debug == True:
        print("wait_for_proto_message_ext ip:{0}, port:{1}\n".format(ip, port))
    oMessageSubscriber = Subscriber()
    oMessageSubscriber.connect(ip, port)

    fnChainRespCallback = self.oGenericProtoManager.oChainResponsibility.call_function(sChainRespCallback)
    fnChainRespCallbackFailure = self.oGenericProtoManager.oChainResponsibility.call_function(sChainRespCallbackFailure)
    while self.is_running:
        try:
            topic = oMessageSubscriber.receive_msg()
            server_msg = oMessageSubscriber.receive_msg()
            sTopic = topic.decode()
            if oServerTopic.__contains__(sTopic) == True:  # Module.topic is registered to this oMessageSubscriber.connect(ip, port) server
                oParsedMsg, objProtoWrapper = self.message_factory_parse(sTopic, server_msg)
                if objProtoWrapper != None:
                    objProtoWrapper.callback(self.oGenericProtoManager.oChainResponsibility, objProtoWrapper, oParsedMsg)
                    try: #if Protobuf was defined using config.message to log in csv, put data in queue
                        if objProtoWrapper.write_csv == True:
                            csv_name = objProtoWrapper.module_name + objProtoWrapper.topic
                            if self.oTopicCSVLock[csv_name] != None:

                                frequency_approve_flag = False # Enable restriction of incoming topic (limit frequency)
                                # Enable restriction of incoming topic
                                if objProtoWrapper.csv_frequency_sec > 0:
                                    objProtoWrapper.keep_time = time.time()
                                    fTimeDelta = objProtoWrapper.keep_time - objProtoWrapper.start_time
                                    if fTimeDelta >= objProtoWrapper.csv_frequency_sec:
                                        frequency_approve_flag = True
                                else:
                                    frequency_approve_flag = True

                                if frequency_approve_flag == True:
                                    oLock = self.oTopicCSVLock[csv_name]
                                    with oLock: #.acquire(True)
                                        self.oTopicCSVQMsg[csv_name].put(oParsedMsg)
                                    objProtoWrapper.start_time = objProtoWrapper.keep_time
                            #oLock.release()
                    except:
                        pass
                else:
                    fnChainRespCallback(self.oGenericProtoManager.oChainResponsibility, server_msg)
        except Exception as e:
            sErrr = str(e)
            logger.debug("Error wait_for_proto_message error:{0}".format(sErrr))
            fnChainRespCallbackFailure(self.oGenericProtoManager.oChainResponsibility, (sErrr, e.args))

    logger.info("End wait_for_proto_message")

# If defined, log csv for arrived protobuf
def wait_log_proto_message_to_csv(self, topic, module_name, oLock):
    logger.info("Start wait_log_proto_message_to_csv module_name:{0} topic:{1}".format(module_name, topic))
    today = datetime.now()
    year = str(today.year)
    month = str(today.month)
    day = str(today.day)
    hour = str(today.hour)
    minute = str(today.minute)
    sec = str(today.second)
    name = year + "_" + month + "_" + day + "__" + hour + "_" + minute + "_" + sec + ".csv"

    path = ""
    if sys.platform == 'win32':
        path += PROJECT_ROOT + '..\\..\\..\\CSV\\' + module_name + '\\' + topic + '\\'
    else:
        path += PROJECT_ROOT + '../../../CSV/' + module_name + '/' + topic + '/'

    if not os.path.exists(path):
        os.makedirs(path)

    path += name

    # Get message attributes for CSV columns
    modules = self.oGenericProtoManager.modules
    oTopics = modules[module_name]
    oMsg = oTopics[topic]
    oCols = []
    for attr in oMsg:
        oCols.append(attr)
    csv_name = module_name + topic
    #No need to lock since it occurs once when worker thread is first called once for each module + topic
    try:
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(oCols)
    except:
        self.oTopicCSVLock[csv_name] = None #If CSV file was failed to be created set module+topic related, lock to None to prevent messages to be CSV logged
        logger.info("wait_log_proto_message_to_csv, CSV file, {0}, was failed to be created, related {1}.{2} won't be CSV logged".format(path, module_name, topic))

    logger.info("wait_log_proto_message_to_csv, created CSV file:{0}".format(path))

    csv_name = module_name + topic
    if self.oConfig.debug == True:
        print("wait_log_proto_message_to_csv module_name:{0}, topic:{1}\n".format(module_name, topic))

    while self.is_running:
       try:
            oRows = []
            with oLock: #.acquire(True)
                oQueue = self.oTopicCSVQMsg[csv_name]
                while not oQueue.empty():
                    oRow = []
                    oRows.append(oRow)
                    oParsedMsg = oQueue.get()
                    for attr in oParsedMsg:
                        oRow.append(oParsedMsg[attr])
            #oLock.release()
            if len(oRows) > 0:
                with open(path, 'a') as file:
                    writer = csv.writer(file)
                    writer.writerows(oRows)

            time.sleep(5)
       except:
           pass


# Manage Communication - Bind to publish, Connect to subscribe to zmq
# Create Protobuf message, register message handler by topic (Chain Responsibility Callback pattern) for farther engine call when message received
class CommunicationManager(object):
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(CommunicationManager, cls).__new__(cls)
            cls.instance.__initialize()
        return cls.instance

    def __initialize(self):
        self.is_running = False
        self.oGenericProtoManager = GenericProtoManager()
        self.thSubArr = []
        self.oFilterTopicByURL = {} #If topic was subscribed to Publisher A and can be arrived also from Publisher B, add here this Topic so, it will use only Publisher A
        self.oConfig = Configuration()
        self.oMessagePublisher = Publisher()
        self.oMessagesFactory = {}  # Keep and create message by topic
        self.fnChainResponsibilityCallback = {}  # After sending message, this is a callback for chain responsibility function (determines behavior after sending message usually an Emgine related function)
        self.oUtil = Util()
        self.oTopicCSVLock = {}
        self.oTopicCSVQMsg = {}

    def start(self):
        if self.is_running == False:
            self.is_running = True
            logger.info("Start CommunicationManager")
            self.__start_subscribe_threads()

    def __start_subscribe_threads(self):
        for idx, th in enumerate(self.thSubArr):
            th.start()

    def stop(self):
        if self.is_running == True:
            self.is_running = False
            self.oFilterTopicByURL = {}
            logger.info("Stop CommunicationManager")

    def __filter_topic_from_backend_rec_msg(self, topic):
        if topic in self.oFilterTopicByURL:
            return True
        else:
            return False

    # Register servers according to created list made from config file and available modules
    def register(self, oServer, oServerTopic, fnChainRespCallback, fnChainRespCallbackFailure):
            #self.thSubArr.append(threading.Thread(target=wait_for_proto_message, args=(self, oTopicsCSV, oServerTopic, fnChainRespCallback, fnChainRespCallbackFailure), daemon=True))
            self.thSubArr.append(threading.Thread(target=wait_for_proto_message, args=(self, oServer, oServerTopic, fnChainRespCallback, fnChainRespCallbackFailure), daemon=True))
            # Register servers according to created list made from config file and available modules

    def registerCSV(self, oTopicsCSV):
        #self._oTopicCSV[module_name+k] = {'module_name': module_name, 'topic': k, 'write_csv': write_csv, 'csv_frequency_sec': csv_frequency_sec}
        topic = self.oUtil.help_set_if_exist(oTopicsCSV, "topic", "")
        module_name = self.oUtil.help_set_if_exist(oTopicsCSV, "module_name", "")
        if self.oUtil.help_set_if_exist(oTopicsCSV, "write_csv", False) == True and topic != "" and module_name != "":
             oLock = threading.Lock()
             csv_name = module_name+topic
             self.oTopicCSVLock[csv_name] = oLock
             oQqueue = queue.Queue()
             self.oTopicCSVQMsg[csv_name] = oQqueue
             self.thSubArr.append(threading.Thread(target=wait_log_proto_message_to_csv, args=(self, topic, module_name, oLock), daemon=True))

    # Make sure topic is decoded
    # Determine Message class factory and parse message string into message protobuf
    def message_factory_parse(self, topic, msg_str):
        return  self.oGenericProtoManager.message_factory_parse(topic, msg_str)

    def send_message(self, msg, topic):
        self.oMessagePublisher.publish_msg(msg.SerializeToString(), topic=topic.encode())


