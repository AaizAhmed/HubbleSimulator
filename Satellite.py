# This class generated data and stores it in a buffer

import threading
import random
import Buffer

class Satellite(threading.Thread):

    buffer = None

    def __init__(self):

        buffer = Buffer.Buffer()

