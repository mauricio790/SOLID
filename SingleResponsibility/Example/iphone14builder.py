from iphonebuilder import iphonebuilder
from iphone14 import iphone14

class iphone14builder(iphonebuilder):
    phone = None
        
    def __init__(self):
        self.reset()

    def reset(self):
        self.phone = iphone14()

    def setCameras(self):
        print("2 cameras")

    def setSize(self):
        print("13 cm x 5 cm")

    def series(self):
        print("13.1")

    def getIphone(self):
        return self.phone