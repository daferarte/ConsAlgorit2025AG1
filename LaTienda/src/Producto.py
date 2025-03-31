__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from Tipo import Tipo

class Producto:
    
    ###################################################
    # constantes
    ###################################################
    
    IVA_PAPELERIA:float=0.16
    IVA_SUPERMERCADO:float=0.04
    IVA_FARMACIA:float=0.12
    
    ###################################################
    # Constructor
    ###################################################
    
    def __init__(self, nombre:str, tipo:Tipo, valorUnitario:float, cantidadBodega:int, subsidio:bool, calidad:str, cantidadMinima:int):
        ###################################################
        # Atributos
        ###################################################
        self.__nombre:str=nombre
        self.__tipo:Tipo=tipo
        self.__valorUnitario:float=valorUnitario
        self.__cantidadBodega:int=cantidadBodega
        self.__subsidio:bool=subsidio
        self.__calidad:str=calidad
        self.__cantidadMinima:int=cantidadMinima
        
    __method__="DarNombre"
    __params__="Ninguno"
    __return__="Nombre"
    __description__="Metodo que sirve para dar el nombre de el producto"
    def DarNombre(self):
        return self.__nombre
    
    __method__="CambiarNombre"
    __params__="Nombre"
    __return__="Nada"
    __description__="Metodo que sirve para cambiar el nombre de el producto"
    def CambiarNombre(self, nombre:str):
        self.__nombre=nombre
    
    

        
        