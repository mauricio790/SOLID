from Character import Mago

class AsesinoMago(Mago):
    def presentacion(self):
        print("Rol: ")
        self.definicion()
        print("Ataque: ")
        self.ataque()
        print("Habilidades: ")
        self.hechizo()
        self.teleport()