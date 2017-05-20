# This class receives the data from the buffer

from threading import Thread


class Receiver(Thread):

    _buff = None
    _local_buffer = None
    _size = 0


    def __int__(self, buffer, size):
        Thread.__init__(self)

        self._buff = buffer
        self._local_buffer = list()
        self._size = size


    def run(self):
        print('Size/2 =', self._size/2)
        for index in range(self._size/2):
            num = self._buff.pop(0)
            self._local_buffer.append(num)
            print('Receiver', num)


