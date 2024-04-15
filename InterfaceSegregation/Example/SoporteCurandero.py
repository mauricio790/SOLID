from Character import Curandero

class SoporteCurandero(Curandero):
    def presentacion(self):
        print("Rol: ")
        self.definicion()
        print("Ataque: ")
        self.ataque()
        print("Habilidades: ")
        self.curar()
        self.potenciar()