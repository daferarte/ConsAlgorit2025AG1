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
        self.nombre:str=nombre
        self.tipo:Tipo=tipo
        self.valorUnitario:float=valorUnitario
        self.cantidadBodega:int=cantidadBodega
        self.subsidio:bool=subsidio
        self.calidad:str=calidad
        self.cantidadMinima:int=cantidadMinima
        
        