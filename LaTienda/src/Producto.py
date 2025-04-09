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
    
    def __init__(self, nombre:str, tipo:Tipo, valorUnitario:float, cantidadBodega:int, calidad:str, cantidadMinima:int):
        ###################################################
        # Atributos
        ###################################################
        # if not nombre:
        #     return "el nombre no puede ser vacio"
        # if valorUnitario<0:
        #     return "el valor unitario debe ser mayor a 0"
        
        assert nombre, "el nombre no puede ser vacio"
        assert tipo in Tipo, "no esta contemplado el tipo"
        
         
        self.__nombre:str=nombre
        self.__tipo:Tipo=tipo
        self.__valorUnitario:float=valorUnitario
        self.__cantidadBodega:int=cantidadBodega
        self.__subsidio:bool=False
        self.__calidad:str=calidad
        self.__cantidadMinima:int=cantidadMinima
        self.__candidadUnidadesVendidas:int=0
        
    __method__="DarNombre"
    __params__="Ninguno"
    __return__="Nombre"
    __description__="Metodo que sirve para dar el nombre de el producto"
    def DarNombre(self):
        return self.__nombre
    
    __method__="CambiarNombre"
    __params__="Nombre"
    __return__="Nada"
    __description__="Metodo que sirve para cambiar el nombre del producto"
    def CambiarNombre(self, nombre:str):
        assert nombre, 'El nombre no puede ser vacio'
        self.__nombre=nombre
        
    __method__="DarValorUnitario"
    __params__="Ninguno"
    __return__="ValorUnitario"
    __description__="Metodo que sirve para dar el valor unitario del producto"
    def DarValorUnitario(self):
        return self.__valorUnitario
    
    __method__="CambiarValorUnitario"
    __params__="ValorUnitario"
    __return__="Nada"
    __description__="Metodo que sirve para cambiar el valor unitario del producto"
    def CambiarValorUnitario(self, valorUnitario:str):
        self.__valorUnitario=valorUnitario
    
    
    __method__="Vender"
    __params__="cantidad"
    __return__="Mensaje de resultado"
    __description__="Metodo que sirve para vender productos"
    def vender(self, cantidad:int):
        # if cantidad <= 0:
        #     return 'Ingresa una cantidad mayor a 0'
        assert cantidad > 0, 'Ingresa una cantidad mayor a 0'
        # aqui va el codigo
        if cantidad <= self.__cantidadBodega: 
            self.__candidadUnidadesVendidas+=cantidad
            self.__cantidadBodega-=cantidad
            return f'Se vendieron {cantidad} unidades de {self.__nombre} con exito'
        else:
            return f'No se pueden vender {cantidad} unidades de {self.__nombre}, porque no existe disponibilidad en bodega'
        
    
    __method__="HaySuficientes"
    __params__="cantidad"
    __return__="booleano"
    __description__="Metodo que sirve para saber si hay suficientes unidades en bodega"
    def HaySuficientes(self, cantidad:int):
        # aqui va el codigo
        # Forma 1
        # suficiente:bool
        
        # if cantidad <= self.__cantidadBodega: 
        #     suficiente=True
        # else:
        #     suficiente=False
            
        # return suficiente
    
        # Forma 2 
        # suficiente:bool = False
        
        # if cantidad <= self.__cantidadBodega: 
        #     suficiente=True
            
        # return suficiente

        # Forma 3
        
        return cantidad <= self.__cantidadBodega
    
    
    __method__="DarPrecioPapeleria"
    __params__="conIva"
    __return__="precioFinal"
    __description__="Metodo que sirve para dar el precio final de un producto de papeleria"
    def DarPrecioPapeleria(self, conIva):
        # aqui inicia el codigo
        
        precioFinal:float=self.__valorUnitario
        
        if conIva:
            precioFinal *=(1+self.IVA_PAPELERIA)
        
        return precioFinal
    
    __method__="AjustarPrecio"
    __params__="ninguno"
    __return__="Mensaje de confirmacion"
    __description__="Metodo que sirve para ajustar el valor unitario del producto"
    def AjustarPrecio(self):
        # aqui va el codigo
        if self.__candidadUnidadesVendidas < 100:
            self.__valorUnitario *= (80/100)
            return f'Tu producto ahora cuesta {self.__valorUnitario}, aplicado 80% de descuento'
        else:
            self.__valorUnitario *= 1.1 
            return f'Tu producto ahora cuesta {self.__valorUnitario}, aplicado 10% de incremento'
        
    __method__="DarIVA"
    __params__="ninguno"
    __return__="IVA"
    __description__="Metodo que sirve para conocer el iva del producto"
    def DarIVA(self):
        # aqui va el codigo
        # Forma 1
        # if self.__tipo == Tipo.PAPELERIA:
        #     return self.IVA_PAPELERIA
        # elif self.__tipo == Tipo.FARMACIA:
        #     return self.IVA_FARMACIA
        # else:
        #     return self.IVA_SUPERMERCADO
        
        # Forma 2
        iva:float=0.0
        if self.__tipo == Tipo.PAPELERIA:
            iva= self.IVA_PAPELERIA
        elif self.__tipo == Tipo.FARMACIA:
            iva= self.IVA_FARMACIA
        else:
            iva= self.IVA_SUPERMERCADO
        
        return iva