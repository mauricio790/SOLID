# Definición de la interfaz general para personajes
class Personaje:
    def definicion(self):
        pass

    def atacar(self):
        pass

# Interfaz para el tipo de personaje Tanque
class Tanque(Personaje):
    def definicion(self):
        print("Tanque.")

    def ataque(self):
        print("Ataque a cuerpo.")

    def golgpeCritico(self):
        print("Golpe crítico.")

    def bloqueo(self):
        print("Bloqueo de daño con escudo.")

# Interfaz para el tipo de personaje Mago
class Mago(Personaje):
    def definicion(self):
        print("Mago.")

    def ataque(self):
        print("Ataque a distancia.")

    def hechizo(self):
        print("Invocamiento de hechizo.")
        
    def teleport(self):
        print("Teletrasportacion a lugar seguro.")

# Interfaz para el tipo de personaje Curandero
class Curandero(Personaje):
    def definicion(self):
        print("Curandero.")

    def ataque(self):
        print("Ataque a distancia.")

    def curar(self):
        print("Curar heridas.")

    def potenciar(self):
        print("Fortalecer aliados.")