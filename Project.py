# This class runs the Satellite simulation and
# runs are the threads

import Receiver
import Satellite
import Buffer

def RunSatellite():

    buffer = Buffer.Buffer(5)
    buff = buffer.getBuffer()

    satellie = Satellite.Satellite(buff)
    satellie.add()
    satellie.add()

    print( len(buff) )

    receiver = Receiver.Receiver(buff)

    satellie.join()
    receiver.join()

RunSatellite()


