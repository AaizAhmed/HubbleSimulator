# This class receives the data from the buffer

from threading import Thread

class Receiver(Thread):

    _buff = None
    _local_buffer = None

    def __int__(self, buffer):
        Thread.__init__(self)

        self._buff = buffer
        self._local_buffer = list()


