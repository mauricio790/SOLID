## Dependency Inversion

### Definición

El principio de inversión de dependencias indica que no se debe de depender de clases o funciones concretas, sino que se depende de clases abstracatas. Así se evitan los efectos secundarios y la frecuencia en la que se requieren realizar cambios. 

### Ejemplo

Este principio de inversión de independencias se ha demostrado en diversos ejemplos en este proyecto. 

#### Ejemplo 1. 

[S - SOLID](../SingleResponsibility/Example)

En este ejemplo la clase iphone actúa como interfaz abstrayendo las características principales de los teléfonos iPhone.

``` python
class iphone: 
    series = ""
    cameras = 0
    size = ""
```

Luego las clases iPhone14 y iPhone15pro dependen de la interfaz definida anteriormente. Así cualquier cambio sobre los iPhone recae únicamente en la clase iPhone, esta es la ventaja del principio de inversión de dependencias. 

##### iPhone14
``` python
from iphone import iphone

class iphone14(iphone):
    def __init__(self):
        pass

    
```
#### iPhone15pro

``` python 
from iphone import iphone

class iphone15pro(iphone):
    def __init__(self):
        pass
```

#### Ejemplo 2. 

[O - SOLID](../OpenClosed/Example/OCP)

Se observa la misma interacción entre Level - Primaria/Secundaria

##### Level 

``` python
# Abstract class
class Level():
    def __init__(self) -> None:
        pass
    def graduate():
        pass
```

##### Primaria 

```python
from Level import Level

class Primaria(Level):

    def graduate(self):
        return "Educación primaria concluida"
```

##### Secundaria

``` python
from Level import Level

class Secundaria(Level):

    def graduate(self):
        return "Educación secundaria concluida"
```