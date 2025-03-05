__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class CuentaCorriente:
    #Aqui va mi codigo
    saldo = 0
    
    
    ################################
    # Metodos
    ################################
    
    __method__ = "DarSaldo"
    __params__ = "nada"
    __returns__ = "Saldo"
    __descriptions__ = "Este metodo permite conocer el saldo de la cuenta corriente"
    def DarSaldo(self):
        # aqui va mi codigo
        return self.saldo
    
    __method__ = "Consignar"
    __params__ = "monto"
    __returns__ = "nada"
    __descriptions__ = "Este metodo permite consignar un monto a la cuenta corriente"
    def Consignar(self, monto):
        # aqui va mi codigo
        self.saldo = self.saldo + monto
    
    __method__ = "Retirar"
    __params__ = "monto"
    __returns__ = "nada"
    __descriptions__ = "Este metodo permite retirar un monto de la cuenta corriente"
    def Retirar(self, monto):
        # aqui va mi codigo
        self.saldo = self.saldo - monto