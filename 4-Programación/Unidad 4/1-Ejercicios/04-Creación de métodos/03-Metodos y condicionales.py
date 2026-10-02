class CuentaBancaria():
    def __init__(self):
        self.saldo = 0
        
    def retirarSaldo(self, cantidad):
        if cantidad < 10000:
            if cantidad < self.saldo:
                    self.saldo = self.saldo - cantidad
                    print("Operación relizada con exito, su saldo actual es de:",self.saldo)
            else: 
                print("Saldo insuficiente, consiga dinero roedor")
                
                
    def depositarSaldo(self, cantidad):
        if cantidad < 1:
            print("El monto a depositar, debe ser superior a 0 €, VACILÓN")
        else:
            if cantidad > 9999:
                print("Notificando a la entidad")
                
            self.saldo = self.saldo + cantidad
            print("Depósito realizado. Saldo:", self.saldo)
        
Micuenta1 = CuentaBancaria()
Micuenta1.depositarSaldo(0)


Micuenta2 = CuentaBancaria()
Micuenta2.depositarSaldo(10000)

Micuenta2.retirarSaldo(500)

        