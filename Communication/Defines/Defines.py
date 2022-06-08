from Communication.Include.Config import Configuration
import logging
logger = logging.getLogger(__name__)

class Util(object):
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(Util, cls).__new__(cls)
        return cls.instance

    def help_set_if_exist(self, oItem, key, default_value):
        try:
            if oItem.__contains__(key) == True:
                return oItem[key]
        except:
            pass

        return default_value
