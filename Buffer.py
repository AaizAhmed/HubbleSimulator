# This class stores data in a thread safe list.

from threading import Thread

class Buffer(Thread):

    _buffer_list = None
    _size = None

    def __init__(self, size):
        Thread.__init__(self)

        self._size = size
        self._buffer_list = list()

    def add(self, number):

        if len(self._buffer_list) <= self._size:
            self._buffer_list.append(number)

    def getBuffer(self):
        return self._buffer_list

