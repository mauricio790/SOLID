## Interface Segregation

### Definición

El principio de Interface Segregation promueve la creación de interfaces específicas y cohesivas para diferentes partes de un sistema, en lugar de tener una única interfaz general que contenga métodos irrelevantes para algunas partes del sistema. Indica que no se debe depender de interfaces que no se necesitan. De esta manera se evitan efectos secundarios de cambios y es más fácil agregar funcionalidades sin afectar clases existentes.

### Ejemplo

#### Problema
Estamos diseñando un sistema de roles para personajes de un videojuego. Tenemos una interfaz Personaje que inicialmente contiene los metodos definicion() y ataque():

``` python 
# Definición de la interfaz general para personajes
class Personaje:
    def definicion(self):
        pass
    def ataque(self):
        pass
```

Y luego se agregan métodos específicos dependiendo del rol primario de un personaje: 

```python
# Definición de la interfaz general para personajes
class Personaje:
    def definicion(self):
        pass
    def ataque(self):
        pass

    # Tanque
    def golgpeCritico(self):
        print("Golpe crítico.")
    def bloqueo(self):
        print("Bloqueo de daño con escudo.")

    # Magos
    def hechizo(self):
        print("Invocamiento de hechizo.")        
    def teleport(self):
        print("Teletrasportacion a lugar seguro.")

    # Curanderos
    def curar(self):
        print("Curar heridas.")
    def potenciar(self):
        print("Fortalecer aliados.")
```
Esto implica que cada clase que herede de esta interfaz, necesita implementar todos los métodos aún si su rol no lo indica. Aquí se rompe el principio de Interface Segregation. 

#### Solución

Para cumplir con este principio, separamos esta interfaz en interfaces más específicas como lo serían Tanque(Personaje), Mago(Personaje) y Curandero(Personaje):

```python 
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
        print("Ataque a distancia")

    def curar(self):
        print("Curar heridas.")

    def potenciar(self):
        print("Fortalecer aliados.")
```

De esta manera se cumple con el principio de Interface Segregation y así podemos crear clases concretas para la definición específica de roles, por ejemplo AsesinoMago(Mago): 

```python
from Character import Mago

class AsesinoMago(Mago):
    def presentacion(self):
        print("Rol:")
        self.definicion()
        print("Ataque:")
        self.ataque()
        print("Habilidades:")
        self.hechizo()
        self.teleport()
``` 

O inclusive el mismo tipo de personaje que depende de interfaces distintas como SoporteCurandero(Curandero) o SoporteTanque(Tanque):

```python
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
```

```python
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
```

### Ejecución del ejemplo

```bash
md Example/ 
python App.py 
```

#### Salida

```bash
Diana seleccionada: 
Rol:
Mago.
Ataque:
Ataque a distancia.
Habilidades:
Invocamiento de hechizo.
Teletrasportacion a lugar seguro.

Nami seleccionada:
Rol:
Curandero.
Ataque:
Ataque a distancia.
Habilidades:
Curar heridas.
Fortalecer aliados.

Nautilus seleccionado:
Rol:
Tanque.
Ataque:
Ataque a cuerpo.
Habilidades:
Golpe crítico.
Bloqueo de daño con escudo.
```