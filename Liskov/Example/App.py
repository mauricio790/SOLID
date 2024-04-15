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