import timestamp_pb2
import datetime

class TimeProtobuf:
    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(TimeProtobuf, cls).__new__(cls)
        return cls.instance


    def set_time_stamp(self):
        messageTime = timestamp_pb2.Timestamp()
        oDate = datetime.datetime.now()
        seconds_since_epoch = oDate.replace(tzinfo=datetime.timezone.utc).timestamp()
        messageTime.seconds = int(seconds_since_epoch)
        messageTime.nanos = self.__sec_fraction_to_nano(seconds_since_epoch)
        return messageTime
        # retrieves offset for seconds fraction since epoch time


    def __sec_fraction_to_nano(self, seconds_since_epoch):
        sSec = str(seconds_since_epoch)
        nPos = sSec.find(".")
        if nPos == -1:
            return 0
        sSecFrac = sSec[nPos:sSec.__len__()]
        return int(float(sSecFrac) * 1000000000)