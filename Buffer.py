# This class stores data in a thread safe list.

import threading

class Buffer(threading.Thread):

    buffer_list = None

    def __init__(self):

        self.buffer_list = list()

