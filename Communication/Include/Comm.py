import zmq
"""Liad Kashanovsky - ZMQ Communication Manager. Subscribe per topic"""

class Subscriber(object):
    def __init__(self):
        self.context = None
        self.socket = None
        self.ip = None
        self.port = None

    def subscribe(self, topic):
        self.socket.subscribe(topic)

    def connect(self, ip=None, port=None):
        self.ip = ip if ip is not None else "127.0.0.1"
        self.port = port if port is not None else "5556"
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.setsockopt_string(zmq.SUBSCRIBE, "")
        self.socket.connect("tcp://%s:%s" % (self.ip, self.port))

    def receive_msg(self, topic_filter=None):
        if topic_filter is not None:
            self.socket.setsockopt_string(zmq.SUBSCRIBE, str(topic_filter))
            msg = self.socket.recv()
        else:
            msg = self.socket.recv()
        return msg


class Publisher:
    port = None
    context = None
    socket = None

    def __new__(cls):
        """ creates a singleton object, if it is not created,
        or else returns the previous singleton object"""
        if not hasattr(cls, 'instance'):

            cls.instance = super(Publisher, cls).__new__(cls)
            cls.instance.context = zmq.Context()
            cls.instance.socket = cls.instance.context.socket(zmq.PUB)

        return cls.instance

    def bind(self, ip, port):
        self.socket.bind("tcp://%s:%s" % (ip, port))

    def publish_msg(self, msg, topic=None):
        # self.socket.send_string("%s %s" % (topic, msg))
        if topic is not None:
            self.socket.send_multipart([topic, msg])
        else:
            self.socket.send(msg)
