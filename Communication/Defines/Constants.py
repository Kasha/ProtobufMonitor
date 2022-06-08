from enum import Enum

class NIART_INS_ERROR_IDS(Enum):
     OK = 0
     GENERAL_ERROR = 1
     SERIAL_PORT_FAILURE = 2
     MISSING_GPS_PARSER = 3
     INVALID_PARSER_BUFFER = 4

class NIART_INS_ERROR_TXT(Enum):
    OK = "OK"
    GENERAL_ERROR = "Unknown error"
    SERIAL_PORT_FAILURE = "Can't access Serial Port"
    MISSING_GPS_PARSER = "Missing GPS parser handler"
    INVALID_PARSER_BUFFER = "Invalid Parser Buffer Data"

class NIART_INS_LOG_LEVEL(Enum):
    NONE = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    FATAL = 6

class GPS_DATA_PARSER_TYPE(Enum):
    AUTO_DETECT = 0
    GPSD = 1
    ARAZIM = 2

class GPS_DATA_PARSER_NAME_STR(Enum):
    ARAZIM = "Arazim INS/GPS Sensor"
    GPSD = "GPSD Parser for any sensor"

class GPS_DATA_MESSAGE(Enum):
    DATA = '0x30'
    STATISTICS = '0x32'
    INS = '0x52'
