from enum import Enum

class Level(Enum):
    PRIMARIA = 0
    SECUNDARIA = 1

class StudentNoOPC():
    def __init__(self):
        pass
    
    def graduate(level):
        # Graduate according to education level
        if(level == Level.PRIMARIA.value):
            print("Educación primaria concluida")
        elif(level == Level.SECUNDARIA.value):
            print("Educación secundaria concluida")