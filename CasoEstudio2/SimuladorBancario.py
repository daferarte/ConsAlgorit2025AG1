__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

################################################################
# Importaciones
################################################################

from CuentaCorriente import CuentaCorriente
from CuentaAhorros import CuentaAhorros
from CDT import CDT

class SimuladorBancario:
    #Aqui va mi codigo
    nombre = ''
    cedula = ''
    mesActual = ''
    
    # asociaciones
    cuentaAhorros = CuentaAhorros()
    cuentaCorriente = CuentaCorriente()
    cdt = CDT()
    
    ################################
    # Metodos
    ################################
    
    __method__ = "ConsignarCuentaCorriente"
    __params__ = "monto"
    __returns__ = "nada"
    __descriptions__ = "Este metodo permite consignar un monto a la cuenta corriente"
    def ConsignarCuentaCorriente(self, monto):
        # aqui va mi codigo
        self.cuentaCorriente.Consignar(monto)
    
    __method__ = "CalcularSaldoTotal"
    __params__ = "nada"
    __returns__ = "SaldoTotal"
    __descriptions__ = "Este metodo permite calcular el saldo total de las cuentas ahorros, corriente y CDT"
    def CalcularSaldoTotal(self):
        # aqui va mi codigo
        
        # Forma 1
        """
        saldoTotal = self.cuentaAhorros.DarSaldo()
        saldoTotal = saldoTotal + self.cuentaCorriente.DarSaldo()
        saldoTotal = saldoTotal + self.cdt.DarSaldo()
        
        return saldoTotal
        """
        # Forma 2
        # saldoTotal = self.cuentaCorriente.DarSaldo()+self.cdt.DarSaldo()+self.cuentaAhorros.DarSaldo()
        # return saldoTotal
        
        # Forma 3
        
        return self.cuentaCorriente.DarSaldo() + self.cdt.DarSaldo() + self.cuentaAhorros.DarSaldo()
    
    __method__ = "PasarAhorrosCorriente"
    __params__ = "ninguno"
    __returns__ = "nada"
    __descriptions__ = "Este metodo permite pasar los ahorros de la cuenta ahorros a la cuenta corriente"
    def PasarAhorrosCorriente(self):
        # aqui va mi codigo
        saldoAhorros = self.cuentaAhorros.DarSaldo()
        self.cuentaAhorros.Retirar(saldoAhorros)
        self.cuentaCorriente.Consignar(saldoAhorros)
    
    