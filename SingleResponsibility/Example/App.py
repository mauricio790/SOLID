from Director import Director
from iphone14builder import iphone14builder
from iphone15probuilder import iphone15probuilder

class App():
    def __init__(self):
        pass
    def makeIphone(self):
        director = Director()

        builder = iphone14builder()
        director.buildiphone14(builder)
        iphone14 = builder.getIphone()

        print(iphone14)

        
        builder = iphone15probuilder()
        director.buildiphone15pro(builder)
        iphone15 = builder.getIphone()
        print(iphone15)

app = App()
app.makeIphone()