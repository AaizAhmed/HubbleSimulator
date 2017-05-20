# This class runs the Satellite simulation and
# runs are the threads

import Receiver
import Satellite
import Buffer

def RunSatellite():

    # Add the FOR loops first

    buffer = Buffer.Buffer(10)
    buff = buffer.getBuffer()

    satellie = Satellite.Satellite(buff, 10)
    satellie.start()

    satellie.join()

    receiver = Receiver.Receiver(buff, 10)
    receiver.start()

    receiver.join()

RunSatellite()


