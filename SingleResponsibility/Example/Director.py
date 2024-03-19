from iphone14builder import iphone14builder
from iphone15probuilder import iphone15probuilder

class Director:

    def __init__(self):
        pass

    def buildiphone14(self, builder : iphone14builder):
        builder.reset()
        builder.setCameras()
        builder.series()

    def buildiphone15pro(self, builder : iphone15probuilder):
        builder.reset()
        builder.setCameras()
        builder.series()