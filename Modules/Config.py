import yaml
import os
"""Liad Kashanovsky - Monitor, Config file"""

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
CONFIGSETUP = 'Local'
"""Default = Local config, 
Localconfig.yaml, for dev
config.yaml, for production
Localconfig.yaml is excluded from git so config.yaml will be used for Production
"""

class Configuration(object):
    #Default config attributes  and values
    config = {
                'debug': False,
                'info': True,
                'log_level': 20,
                'form_width': 600,
                'form_height': 600,
                'tab_width': 400,
                'tab_height': 480,
                'gatewayID': 'ProtobufMonitor'
              }

    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Configuration, cls).__new__(cls)
            path = PROJECT_ROOT

            if CONFIGSETUP != "Default":
                config_file_name = CONFIGSETUP + 'Config.yaml'
                if path == "":
                    path = './../Configurations/config.yaml'
                elif path.find("/") != -1:# For Linux
                    if os.path.isfile(path + '/../Configurations/' + config_file_name):
                        path += ('/../Configurations/' + config_file_name)
                    else:
                        # SystemEventMsg for not existing communication config file
                        print('The required Main config file does not exist, using global config.yaml configuration file instead')
                        path += '/../Configurations/config.yaml'
                else:#For Windows
                    if os.path.isfile(path + '\\..\\Configurations\\' + config_file_name):
                        path += ('\\..\\Configurations\\' + config_file_name)
                    else:
                        # SystemEventMsg for not existing communication config file
                        print('The required Main config file does not exist, using global config.yaml configuration file instead')
                        path += '\\..\\Configurations\\config.yaml'
            else:
                if path == "":
                    path = './../Configurations/config.yaml'
                elif path.find("/") != -1:#For Linux
                    path += '/../Configurations/config.yaml'
                else:#For Windows
                    path += '\\..\\Configurations\\config.yaml'

            with open(path) as configFile:
                cls.config = yaml.load(configFile, Loader=yaml.FullLoader)
            for k, v in cls.config.items():
               if k == "server_ip" and v == "all":
                    v = '*'
               cls.instance.__dict__[k] = v # Create pair of Key/Value from config object (config.yaml file or default value array)

        return cls.instance

    def __setattr__(self, name, value):
        raise Exception("Failed to read config.yaml file, using default values")