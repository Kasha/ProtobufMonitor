from Communication.Defines.Defines import *
"""Liad Kashanovsky - ChainResponsibility registered arrived protobuf message - Do Something. They should be registered by 
Communication Manager via Module Manager, explicitly using register method or implicitly using Defines\config.yaml -> messages:callback"""

class ChainResponsibility(object):
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(ChainResponsibility, cls).__new__(cls)
            cls.instance.is_running = False
            cls.instance.oConfig = Configuration()
            cls.instance.oModuleUI = None
        return cls.instance

    # Protobuf Generic Message Registered Callback, ChainResponsibilityCallback - OK.
    def ChainResponsibilityCallback(self, msg):
        if self.oConfig.debug == True:
            print("ChainResponsibilityCallback description:{0}".format(msg))

    # Protobuf Generic Message Registered Callback, ChainResponsibilityCallbackFailure - Failure.
    def ChainResponsibilityCallbackFailure(self, msg, args=None):
        if self.oConfig.debug == True:
            print("ChainResponsibilityCallbackFailure err_args:{0}, description:{1}".format(args, msg))
    #Communication implicit generic call back registration, predefined in Defines\config.yaml -> messages:{...callback:ProtobufCallback}
    def ProtobufCallback(self, msg):
        if self.oConfig.debug == True:
            print("EngineChainResponsibility ProtobuffCallback :{0}".format(msg))

    # Communication implicit generic (second) call back registration, predefined in Defines\config.yaml -> messages:{...callback:Protobuf1Callback}
    def Protobuf1Callback(self, objProtoWrapper, msg):
        # Update UI of related Protobuf message, attributes
        for attr in msg:
            key = objProtoWrapper.module_name + objProtoWrapper.topic + attr
            if self.oModuleUI.__dict__.__contains__(key) == True:
                self.oModuleUI.__dict__[key].set(str(msg[attr]))
        if self.oConfig.debug == True:
            print("EngineChainResponsibility Protobuff1Callback :{0}".format(msg))

    # Communication implicit PositionData Message call back registration, predefined in Defines\config.yaml -> messages:{... callback: PositionDataCallback}
    def PositionDataCallback(self, objProtoWrapper, msg):
        # Update UI of related Protobuf message, attributes
        for attr in msg:
            key = objProtoWrapper.module_name+objProtoWrapper.topic+attr
            if self.oModuleUI.__dict__.__contains__(key) == True:
                self.oModuleUI.__dict__[key].set(str(msg[attr]))

        if self.oConfig.debug == True:
            print("EngineChainResponsibility PositionDataCallback :{0}".format(msg))
    #Retrives registered Protobuf message call back
    def call_function(self, method_name):
        try:
            return getattr(ChainResponsibility, method_name)
        except:
            return getattr(ChainResponsibility, "ChainResponsibilityCallback")