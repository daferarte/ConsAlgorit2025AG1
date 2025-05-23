__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Pasajero:
    
    def __init__(self, cedula:str, nombre:str):
        self.__cedula=cedula
        self.__nombre=nombre
        
    __method__ = "DarCedula"
    __params__ = "ninguno"
    __returns__ ="cedula"
    __descriptions__ = "Este metodo permite retornar la cedula del pasajero"
    def DarCedula(self) -> str:
        return self.__cedula
    
    __method__ = "CambiarCedula"
    __params__ = "cedula"
    __returns__ ="ninguno"
    __descriptions__ = "Este metodo permite cambiar la cedula del pasajero"
    def CambiarCedula(self, cedula):
        self.__cedula=cedula
        
    __method__ = "DarNombre"
    __params__ = "ninguno"
    __returns__ ="nombre"
    __descriptions__ = "Este metodo permite retornar el nombre del pasajero"
    def DarNombre(self) -> str:
        return self.__nombre
    
    __method__ = "CambiarNombre"
    __params__ = "nombre"
    __returns__ ="ninguno"
    __descriptions__ = "Este metodo permite cambiar el nombre del pasajero"
    def CambiarNombre(self, nombre):
        self.__nombre=nombre