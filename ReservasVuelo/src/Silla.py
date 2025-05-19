__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from enum import Enum
from Pasajero import Pasajero

class Clase(Enum):
    EJECUTIVA = 1
    ECONOMICA = 2

class Ubicacion(Enum):
    VENTANA = 1
    CENTRO = 2
    PASILLO = 3
    

class Silla:
    
    def __init__(self, numero, clase:Clase, ubicacion:Ubicacion, pasajero:Pasajero = None):
        self.__numero:int = numero
        self.__clase:Clase = clase
        self.__ubicacion:Ubicacion = ubicacion
        self.__pasajero:Pasajero = pasajero
        
    __method__ = "DarNumero"
    __params__ = "ninguno"
    __returns__ ="Numero"
    __descriptions__ = "Este metodo permite retornar el numero de la silla"
    def DarNumero(self) -> int:
        return self.__numero
    
    __method__ = "CambiarNumero"
    __params__ = "Numero"
    __returns__ ="ninguno"
    __descriptions__ = "Este metodo permite cambiar el numero de la silla"
    def CambiarNumero(self, numero):
        self.__numero=numero
        
    __method__ = "DarClase"
    __params__ = "ninguno"
    __returns__ ="Clase"
    __descriptions__ = "Este metodo permite retornar la Clase de la silla"
    def DarClase(self) -> int:
        return self.__clase
    
    __method__ = "CambiarClase"
    __params__ = "Clase"
    __returns__ ="ninguno"
    __descriptions__ = "Este metodo permite cambiar la Clase de la silla"
    def CambiarClase(self, clase):
        self.__clase=clase
    
    __method__ = "DarUbicacion"
    __params__ = "ninguno"
    __returns__ ="Ubicacion"
    __descriptions__ = "Este metodo permite retornar la Ubicacion de la silla"
    def DarUbicacion(self) -> int:
        return self.__ubicacion
    
    __method__ = "CambiarUbicacion"
    __params__ = "Ubicacion"
    __returns__ ="ninguno"
    __descriptions__ = "Este metodo permite cambiar la Ubicacion de la silla"
    def CambiarUbicacion(self, ubicacion):
        self.__ubicacion=ubicacion
        
    __method__ = "DarPasajero"
    __params__ = "ninguno"
    __returns__ ="Pasajero"
    __descriptions__ = "Este metodo permite retornar el Pasajero de la silla"
    def DarPasajero(self) -> int:
        return self.__pasajero
        
    __method__ = "AsignarPasajero"
    __params__ = "Pasajero"
    __returns__ ="ninguno"
    __descriptions__ = "Este metodo permite asignar el Pasajero de la silla"
    def CambiarPasajero(self, pasajero:Pasajero):
        self.__pasajero = pasajero
        
    __method__ = "DesasignarSilla"
    __params__ = "ninguno"
    __returns__ ="ninguno"
    __descriptions__ = "Este metodo permite desasignar una silla"
    def DesasignarSilla(self):
        self.__pasajero = None
        
    
    __method__ = "SillaAsignada"
    __params__ = "ninguno"
    __returns__ ="Estado de la silla true = ocupada y false = libre"
    __descriptions__ = "Este metodo permite verificar si una silla esta vacia"
    def SillaAsignada(self) -> bool:
        return self.__pasajero is not None   
    
    
    