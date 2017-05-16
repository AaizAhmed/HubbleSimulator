# This class generated data and stores it in a buffer

from threading import Thread
from random import randint

class Satellite(Thread):

    _buff = None

    def __init__(self, buffer):
        Thread.__init__(self)

        self._buff = buffer

    def add(self):

        num = randint(0, 4096)
        self._buff.append(num)

# def main():
#     sat = Satellite()
# main()



