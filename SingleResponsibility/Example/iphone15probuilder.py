from iphonebuilder import iphonebuilder
from iphone15pro import iphone15pro

class iphone15probuilder(iphonebuilder):
    phone = None
        
    def __init__(self):
        self.reset()

    def reset(self):
        self.phone = iphone15pro()

    def setCameras(self):
        print("3 cameras")

    def setSize(self):
        print("15 cm x 5.8 cm")

    def series(self):
        print("15 pro")

    def getIphone(self):
        return self.phone