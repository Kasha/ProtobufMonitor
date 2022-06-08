import yaml
from Communication.Defines.Constants import *
import os

"""Liad Kashanovsky - ZMQ Communication, Config file"""

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
CONFIGSETUP = 'Local' """Default = Local config, 
Localconfig.yaml, for dev
config.yaml, for production
Localconfig.yaml is excluded from git so config.yaml will be used for Production
"""

class Configuration(object):
    """
    port: COM3 - port Device name e.g. /dev/ttyUSB0 on GNU/Linux or COM3 on Windows.
    baudrate: 921600
    sleep_sync: 0.001 -

     """
    config = {
                'debug': False,
                'info': True,
                'log_level': 20,# level=logging.INFO
                'gatewayID': 'ProtobufMonitor',
                'icd_ver': '1.0.0_ProtobufMonitor',
                'server_ip': '127.0.0.1',
                'server_port': 12344,
                'write_csv': False,
                'csv_frequency_sec': 0,
                'messages': {'mudules_preset': [{'dir': '.'}]}
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
                    path = './../Defines/config.yaml'
                elif path.find("/") != -1:  # For Linux
                    if os.path.isfile(path + '/../Defines/' + config_file_name):
                        path += ('/../Defines/' + config_file_name)
                    else:
                        # SystemEventMsg for not existing communication config file
                        print(
                            'The required Communication config file does not exist, using global config.yaml configuration file instead')
                        path += '/../Defines/config.yaml'
                else:  # For Windows
                    if os.path.isfile(path + '\\..\\Defines\\' + config_file_name):
                        path += ('\\..\\Defines\\' + config_file_name)
                    else:
                        # SystemEventMsg for not existing communication config file
                        print(
                            'The required Communication config file does not exist, using global config.yaml configuration file instead')
                        path += '\\..\\Defines\\config.yaml'
            else:
                if path == "":
                    path = './../Defines/config.yaml'
                elif path.find("/") != -1:  # For Linux
                    path += '/../Defines/config.yaml'
                else:  # For Windows
                    path += '\\..\\Defines\\config.yaml'

            with open(path) as configFile:
                cls.config = yaml.load(configFile, Loader=yaml.FullLoader)
            for k, v in cls.config.items():
               if k == "server_ip" and v == "all":
                    v = '*'
               cls.instance.__dict__[k] = v # Create Key/Value from config object (config.yaml file or default value array)

        return cls.instance

    def __setattr__(self, name, value):
        raise Exception("Failed to read config.yaml file, using default values")