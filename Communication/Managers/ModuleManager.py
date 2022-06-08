import atexit # allow to catch and handle when there is an implicit or explicit exit
import signal
import logging

from Communication.Managers.CommunicationManager import *

"""Liad Kashanovsky - Module  Manager
1. Create a Communication manager for ZMQ Sub/Pub topic filtered Protobuf message communication
2. Create a GenericProto Manager, for loading proto modules with callback and Publisher listening - config
3. Register a Protobuf per topic callback and start working threads listeners and stop them
4. Clean exit
"""
class ModuleManager(object):
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(ModuleManager, cls).__new__(cls)
            cls.instance.__initialize()
        return cls.instance


    def __initialize(self):

        self.is_running = False
        self.oConfig = Configuration()
        self.oGenericProtoManager = GenericProtoManager()
        self.oCommunicationManager = CommunicationManager()

        if self.oConfig.debug == True:
            logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        elif self.oConfig.info == True:
            logging.basicConfig(level=self.oConfig.log_level,
                               format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logger.info("Start Module Manager")

        atexit.register(self.handle_cleanup)

        """k.add_hotkey("ctrl+x", self.handle_cleanup)
        k.add_hotkey("ctrl+c", self.handle_cleanup)
        k.add_hotkey("ctrl+z", self.handle_cleanup)"""

        if sys.platform == 'win32':
            # signal.signal(signal.SIGINT, signal.CTRL_C_EVENT)
            signal.signal(signal.SIGINT, self.handle_cleanup)
            signal.signal(signal.SIGBREAK, self.handle_cleanup)
            # signal.signal(signal.SIGBREAK, signal.CTRL_BREAK_EVENT)
            signal.signal(signal.SIGABRT, self.handle_cleanup)
            signal.signal(signal.SIGILL, self.handle_cleanup)
            signal.signal(signal.SIGSEGV, self.handle_cleanup)
            signal.signal(signal.SIGTERM, self.handle_cleanup)
            # signal.signal(signal.SIG_IGN, Exit_gracefully)
        else:
            signal.signal(signal.SIGINT, self.handle_cleanup)

        oServers = self.oGenericProtoManager.servers
        for key in oServers:
            oServer = oServers[key]
            oServerTopic = self.oGenericProtoManager.get_server_topic(key)
            self.oCommunicationManager.register(oServer, oServerTopic, self.oConfig.callback, self.oConfig.callback_failure)

        oTopicsCSV = self.oGenericProtoManager.topics_csv
        for key in oTopicsCSV:
            oTopicCSV = oTopicsCSV[key]
            self.oCommunicationManager.registerCSV(oTopicCSV)

        self.oCommunicationManager.start()


    def start(self):
        if self.is_running == False:
            self.is_running = True
            logger.info("Start Process")

    def stop(self):
        if self.is_running == True:
            self.is_running = False
            self.oCommunicationManager.stop()
            time.sleep(1)
            logger.info("Stop Process")

    def handle_cleanup(self, a=None, b=None):
        self.stop()

        if a != None:
            logger.info("Cleanup, Exit gracefully. Done.")
            sys.exit(0)