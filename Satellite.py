# This class generated data and stores it in a buffer

from threading import Thread
from random import randint


class Satellite(Thread):

    _buff = None
    _size = 0


    def __init__(self, buffer, size):
        Thread.__init__(self)

        self._buff = buffer
        self._size = size
        # print('Size is', size)


    def run(self):
        while len(self._buff) < self._size:
            # if len(self._buff) < self._size:
            num = randint(0, 4096)
            self._buff.append(num)
            print('Seattle', num)


    def add(self, num):
        print(num)


# def main():
#     sat = Satellite()
# main()



