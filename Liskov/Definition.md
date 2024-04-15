## Liskov substition principle

### Definición

El principio de sustitución de Liskov indica que un objeto de una super clase puede ser sustituido por cualquier objeto de sus subclases sin romper la aplicación. 

### Ejemplo

En este ejemplo las clases CuentaAhorros y CuentaCorriente heredan de una clase CuentaBancaria. Permitiendo así poder recibir como parámetro cualquier objeto que herede de CuentaBancaria y la aplicación funciona independientemente de la sub clase. 

``` python
class CuentaBancaria():
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        print("Depositar desde superclass")
        pass

    def retirar(self, cantidad):
        print("Retirar desde superclass")
        
class CuentaCorriente(CuentaBancaria):
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad           

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

class CuentaDeAhorro(CuentaBancaria):
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        # Se permite retirar hasta un límite de retiro diario
        limiteDiario = 1000
        if cantidad > 0 and cantidad <= self.saldo and cantidad <= limiteDiario:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente o excede el límite de retiro diario")

class cuentaSuper(CuentaBancaria):
    def tipoCuenta(self):
        print(self.__class__.__bases__[0])
``` 
En esta función, se recibe como parámetro un objeto de tipo CuentaBancaria y en los llamados a la función se envían objetos de las subclases sin romper la aplicación. Aquí se está cumpliendo el principio de Liskov.

``` python
def realizarTransacción(cuenta : CuentaBancaria, cantidad):
        cuenta.retirar(cantidad)
        cuenta.depositar(cantidad)
        print("Transacción exitosa")

cuentaCorriente = CuentaCorriente(1000)
cuentaAhorro = CuentaDeAhorro(2000)
cuentaSuper = cuentaSuper(3000)

# Realizar transacciones con las cuentas
realizarTransacción(cuentaCorriente, 500)
realizarTransacción(cuentaAhorro, 800)
```

### Ejecución del ejemplo

```bash
md Example/ 
python App.py 