from Character import Tanque

class SoporteTanque(Tanque):
    def presentacion(self):
        print("Rol: ")
        self.definicion()
        print("Ataque: ")
        self.ataque()
        print("Habilidades: ")
        self.golgpeCritico()
        self.bloqueo()