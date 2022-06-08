from Communication.Include.Config import *
import sys
import os
import importlib.util
from Communication.Include.ChainResponsibilityCallback import *
import time

""" Liad Kashanovsky - 
1. Parses Protobuf messages from modules. Load protbuf x_pb.py modules and parses them
2. Create Wrapper objects and setup:
    - ChainResponsibility Callbacks 
    - Publisher to listen with Protobuf class name as topic (Per Protobuf module or general callback)
    - Filter Protobuf messages to ignore and attributes to hide or display
"""

class GenericProto(object):
    def __init__(self):
        oConfig = Configuration()
        self.msg = None
        self.message_attr = None #filter attribute to display
        self.module_name = ""
        self.topic = ""
        self.attributes = {}
        self.ip = oConfig.server_ip
        self.port = oConfig.server_port
        self.callback = oConfig.callback
        self.write_csv = False
        # Enable restriction of incoming topic (limit frequency)
        self.csv_frequency_sec = 0
        self.start_time = time.time()
        self.keep_time = time.time()

class GenericProtoManager(object):
    #__slots__ = ('__dict__')
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(GenericProtoManager, cls).__new__(cls)
            cls.instance.__initialize()
        return cls.instance

    def get_topics(self):
        return self._oTopics

    topics = property(get_topics)

    def get_modules(self):
        return self._oModulesArr

    modules = property(get_modules)

    def get_protobuf_message_files(self):
        return self._oProtobufMessageFiles

    protobuf_message_files = property(get_protobuf_message_files)

    def get_servers(self):
        return self._oServers

    servers = property(get_servers)

    def get_server_topics(self):
        return self._oServerTopics

    server_topics = property(get_server_topics)

    def get_server_topic(self, name):
        try:
            return self._oServerTopics[name]
        except:
            return None

    def get_topics_csv(self):
        try:
            return self._oTopicCSV
        except:
            return None

    topics_csv = property(get_topics_csv)

    def __import(self, gbl, module_name, ip = "127.0.0.1", port = 5555, _write_csv = False, _csv_frequency_sec = 0, ChainResponsibilityCallback = None, messages_server = None, filter_message = None, message_attr = None):
        oProto = importlib.import_module(module_name)
        gbl[module_name] = oProto
        #self.__dict__[module_name] = oProto
        for k, v in oProto.__dict__.items():#k = topic
            if v.__class__.__name__ == 'GeneratedProtocolMessageType':  # Than k is a topic and v is a class factory for this topic related Message
                 if filter_message != None:
                    if filter_message.__contains__(k):
                        continue #Filtered topic/message that will arrive won't be found in class factory, and will be ignore when recieved

                 oGPMsgWrapper = GenericProto()
                 oGPMsgWrapper.module_name = module_name
                 oGPMsgWrapper.topic = k

                 """Modules/Module/Message subscribe address:
                 1. First set to config server_ip, server_port 
                 2. Check if address is defined per module_preset (mudules_preset[x].server)
                 3. Check if address is defined per module and/or message (mudules_preset[x].messages_server)"""

                 server_ip = ip
                 server_port = port
                 callback = ChainResponsibilityCallback
                 write_csv = _write_csv
                 csv_frequency_sec = _csv_frequency_sec # Enable restriction of incoming topic (limit frequency)

                 if messages_server != None:
                    if messages_server.__contains__("module_server"):
                        oModuleServer = messages_server["module_server"]
                        server_ip = self.__help_set_if_exist(oModuleServer, "ip", ip)
                        server_port = self.__help_set_if_exist(oModuleServer, "port", port)
                        callback = self.__help_set_if_exist(oModuleServer, "callback", ChainResponsibilityCallback)
                        write_csv = self.__help_set_if_exist(oModuleServer, "write_csv", write_csv)
                        csv_frequency_sec = self.__help_set_if_exist(oModuleServer, "csv_frequency_sec", csv_frequency_sec) # Enable restriction of incoming topic (limit frequency)


                    if messages_server.__contains__("message_server"):
                        oModuleMessageServer = messages_server["message_server"]
                        if oModuleMessageServer.__contains__(k):
                            oMessageServer = oModuleMessageServer[k]
                            server_ip = self.__help_set_if_exist(oMessageServer, "ip", ip)
                            server_port = self.__help_set_if_exist(oMessageServer, "port", port)
                            callback = self.__help_set_if_exist(oMessageServer, "callback", ChainResponsibilityCallback)
                            write_csv = self.__help_set_if_exist(oMessageServer, "write_csv", write_csv)
                            csv_frequency_sec = self.__help_set_if_exist(oMessageServer, "csv_frequency_sec", csv_frequency_sec) # Enable restriction of incoming topic (limit frequency)

                 self._oTopicCSV[module_name+k] = {'module_name': module_name, 'topic': k, 'write_csv': write_csv, 'csv_frequency_sec': csv_frequency_sec}

                 oGPMsgWrapper.ip = server_ip
                 oGPMsgWrapper.port = server_port
                 oGPMsgWrapper.callback = self.oChainResponsibility.call_function(callback)
                 oGPMsgWrapper.write_csv = write_csv
                 oGPMsgWrapper.csv_frequency_sec = csv_frequency_sec # Enable restriction of incoming topic

                 server_name = server_ip+str(server_port)
                 self._oServers[server_name] = {"ip":server_ip, "port":server_port}

                 """Attach topic to server - to Publisher if there are more than 1 same topics for same Publisher (Module1.topic1, 
                 Mosule2.topic1) one oServerTopics[k] will approve all these same topics, other wise different modules with same topics will be in a different Servers/Publishers"""
                 oServerTopics = {}
                 if self._oServerTopics.__contains__(server_name) == True:
                    oServerTopics = self._oServerTopics[server_name]
                 else:
                     self._oServerTopics[server_name] = oServerTopics

                 oServerTopics[k] = True

                 if message_attr != None and len(message_attr) > 0:
                     oGPMsgWrapper.message_attr = message_attr
                     #self.set_message_attribute_filter(oGPMsgWrapper, v())

                 oGPMsgWrapper.msg = v# Message class factory

                 if self._oTopics.__contains__(k):# If topic conains such message from another module
                    obj = self._oTopics[k]
                    if type(obj).__name__ != 'list':# Contains one GenericProto object, since there is more than 1 same message protobuf (From different modules) create an array and set oTopics with array
                        arr = []
                        arr.append(obj) # obj is from type GenericProto() wrapping message class factory
                        arr.append(oGPMsgWrapper)
                        self._oTopics[k] = arr
                    else:
                        obj.append(oGPMsgWrapper) #obj is an array, add same message type for another module
                 else:
                    self._oTopics[k] = oGPMsgWrapper  # Topic is string type (topic that arrived in receive_msg() is encoded (bytes type))

                 self.__add_module_topic_attribute(oGPMsgWrapper)

    def __add_module_topic_attribute(self, oGPMsgWrapper):
        try:
            if oGPMsgWrapper != None:
                if oGPMsgWrapper.module_name != None and oGPMsgWrapper.module_name != "":
                    if len(self._oModulesArr) == 0 or self._oModulesArr.__contains__(oGPMsgWrapper.module_name) == False:
                        self._oModulesArr[oGPMsgWrapper.module_name] = {oGPMsgWrapper.topic: {}}
                    else:# Only one kind of topic per module
                        self._oModulesArr[oGPMsgWrapper.module_name][oGPMsgWrapper.topic] = {}
                    self._oModulesArr[oGPMsgWrapper.module_name][oGPMsgWrapper.topic], obj = self.message_attributes(oGPMsgWrapper.msg(), oGPMsgWrapper, oGPMsgWrapper.topic)
        except:
            pass

    def __get_module_set(self, arr, name):
        try:
            if arr != None:
                if arr.__contains__(name) == True:
                    return arr[name]
            else:
                return None
        except:
            return None

    def __help_set_if_exist(self, oItem, key, default_value):
        try:
            if oItem.__contains__(key) == True:
                return oItem[key]
        except:
            pass

        return default_value

    def __initialize(self):
        self.oConfig = Configuration()
        self._oTopics = {}
        self._oModulesArr = {} #Module.topic.attributes
        self._oProtobufMessageFiles = []
        self._oServers = {}  # Servers list to subscribe to
        self._oServerTopics = {}  # List of Topics that belongs to this server
        self._oTopicCSV = {} # List of Topics to log in CSV according to Frequency [0, when arrives, > 0 any (x) seconds]
        self.oChainResponsibility = ChainResponsibility()
        self.oUtil = Util()

        if self.oConfig.__dict__.__contains__("messages"):
            gbl = globals()
            if self.oConfig.messages.__contains__("mudules_preset"):
                for item in self.oConfig.messages["mudules_preset"]:
                    try:
                        """if item.__contains__("name"):
                            module_name = item["name"]
                            self.__import(gbl, module_name)"""
                        if item.__contains__("dir"):
                            path = item["dir"]
                            if path == '.' or path == "":
                                path = PROJECT_ROOT
                                if sys.platform == 'win32':
                                    path += '\\..\\..\\'
                                else:
                                    path += '/../../'
                                oFilterModules = []
                                if item.__contains__("filter_modules") == True:
                                    oFilterModules = item["filter_modules"]
                                #messages: {mudules_preset: [server:{ip: 127.0.0.1, port: 5554}, {dir: .,filter_modules: [timestamp_pb2.py, GisData_pb2.py], filter_messages:{Common_pb2: {Offset: 1}}, messages_server: {GpsData_pb2: {module_server:{ip: 30.30.30.25, port: 5554}, message_server: {PositionData: { ip: 30.30.30.25, port: 5553}}}}, messages_attr: {GpsData_pb2: {PositionData: { msgHeader: 1, gpsTime: 1, longitude: 1,latitude: 1, altitude: 1, heading: 1, yaw: 1, pitch: 1, roll: 1, velocity: 1} }}}]}

                                """Modules/Module/Message subscribe addressL
                                 1. First set to config server_ip, server_port 
                                 2. Check if address is defined per module_preset (mudules_preset[x].server)
                                 3. Check if address is defined per module and/or message (mudules_preset[x].messages_server)"""
                                ip = self.oConfig.server_ip
                                port = self.oConfig.server_port
                                write_csv = self.oConfig.write_csv
                                csv_frequency_sec = self.oConfig.csv_frequency_sec # Enable restriction of incoming topic (limit frequency)
                                ChainResponsibilityCallback = self.oConfig.callback

                                oServer = None
                                if item.__contains__("server") == True:
                                    oServer = item["server"]
                                    ip = self.oUtil.help_set_if_exist(oServer, "ip", ip)
                                    port = self.oUtil.help_set_if_exist(oServer, "port", port)
                                    ChainResponsibilityCallback = self.oUtil.help_set_if_exist(oServer, "callback", ChainResponsibilityCallback)
                                    write_csv = self.oUtil.help_set_if_exist(oServer, "write_csv", write_csv)
                                    csv_frequency_sec = self.oUtil.help_set_if_exist(oServer, "csv_frequency_sec", csv_frequency_sec)

                                oMessagesServer = None
                                if item.__contains__("messages_server") == True:
                                    oMessagesServer = item["messages_server"]

                                modules = [i[0:i.find('.py')] for i in os.listdir(path) if os.path.isfile(os.path.join(path, i)) and '_pb2' in i and i not in oFilterModules]
                                if len(modules) > 0:
                                    self._oProtobufMessageFiles += modules

                                    oFilterMessages = None
                                    oMessagesAttr = None

                                    if item.__contains__("filter_messages") == True:
                                        oFilterMessages = item["filter_messages"]
                                    if item.__contains__("messages_attr") == True:
                                        oMessagesAttr = item["messages_attr"]

                                    for module_name in modules:
                                        oFilterMessageItem = self.__get_module_set(oFilterMessages, module_name)# Exclude modules.messages/topics in list
                                        oMessageAttrItem = self.__get_module_set(oMessagesAttr, module_name)# Ignore attributes which are not in list
                                        oModuleServerItem = self.__get_module_set(oMessagesServer, module_name)# Server to subscribe to per module and/or messages
                                        self.__import(gbl, module_name, ip, port, write_csv, csv_frequency_sec, ChainResponsibilityCallback, oModuleServerItem, oFilterMessageItem, oMessageAttrItem)
                    except:
                        pass
    #Topic is string type (topic that arrived in receive_msg() is encoded (bytes type))
    def __generic_proto_factory(self, topic):
        try:
            if type(topic).__name__ == "bytes":
                topic = topic.decode()
            if self._oTopics.__contains__(topic) == True:
                return self._oTopics[topic]
            return None
        except:
            return None
    #Return Protobuf message and filtered there is an array of message attributes
    def message_factory_parse(self, topic, msg_buffer):
        try:
            msg, obj = self.__try_message_factory_parse(topic, msg_buffer)
            return self.message_attributes(msg, obj, topic)
        except:
            return None, None

    def message_attributes(self, msg, obj, topic):
        try:
            oParsedMsg = {} #Export protobuf message into array
            if msg != None:
                self.dump_object(msg, oParsedMsg)
                count = len(oParsedMsg)

                if count > 0:
                    if obj != None and obj.message_attr != None:
                        message_attr = obj.message_attr[topic]
                        oParsedMsgTmp = {} # Filtered array with just topic attributes and values according  messages_attr config
                        for k1 in oParsedMsg:
                           for k2 in message_attr:
                               if k2 in k1:
                                   len_key_msg_filter_att = len(k2) * 1.0
                                   len_key_msg_att = len(k1) * 1.0

                                   """ if filter attribute is in message attribute anf eq or 70% eq than use this attribute, 
                                   Allows to write 70% of the word (topic attribute) user wants to show
                                   If topic attribute is an object than just check if filter topic attribute is part or eq to protobuf message key (topic attribute)"""
                                   if len_key_msg_filter_att/len_key_msg_att > 0.8 or k1.find(".") > 0:
                                      oParsedMsgTmp[k1] = oParsedMsg[k1]

                        if len(oParsedMsgTmp) > 0:
                            oParsedMsg = oParsedMsgTmp

                return oParsedMsg, obj
        except:
            return None, None

    def dump_object(self, obj, attRes, name=None):
        for descriptor in obj.DESCRIPTOR.fields:
            value = getattr(obj, descriptor.name)
            if type(value).__name__ == 'RepeatedCompositeContainer':
                attRes[descriptor.name] = value
            elif descriptor.type == descriptor.TYPE_MESSAGE:
                if descriptor.label == descriptor.LABEL_REPEATED:
                    map(self.dump_object, value, attRes, descriptor.name)
                else:
                    self.dump_object(value, attRes, descriptor.name)
            elif descriptor.type == descriptor.TYPE_ENUM:
                enum_name = descriptor.enum_type.values_by_number[value].name
                key = descriptor.name
                if name != None:
                    key = name + "." + key
                attRes[key] = enum_name
                #print "%s: %s" % (descriptor.full_name, enum_name)
            else:
                key = descriptor.name
                if name != None:
                    key = name + "." + key
                attRes[key] = value
                #print "%s: %s" % (descriptor.full_name, value)


    # find the proper protobuf class factory according to topic and also for cases where there are multiple same protobuf for same topic
    def __try_message_factory_parse(self, topic, msg_buffer):
        obj = self.__generic_proto_factory(topic)
        if obj == None:
            return None, None
        try:
            if type(obj).__name__ != 'list':  # Contains GenericProto wrapper with protobuf message
                msg = obj.msg()
                msg.ParseFromString(msg_buffer)
                return msg, obj
        except:
            return None, None

        # Contains list of GenericProto wrappers with same protobuf message  from different modules
        for generic_proto_item in obj:
            try:
               msg = generic_proto_item.msg()
               msg.ParseFromString(msg_buffer)
               return msg, generic_proto_item
            except:
               pass
        return None, None

