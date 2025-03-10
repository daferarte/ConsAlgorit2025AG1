__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Fecha:
    #Aqui va mi codigo
    dia=0
    mes=0
    anio=0
    
    ################################################################
    # Constructor
    ################################################################
    def __init__(self, dia=1, mes=1, anio=1900):
        # aqui va mi codigo
        self.dia = dia
        self.mes = mes
        self.anio = anio
    
    ################################
    # Metodos
    ################################
    __method__ = "DarDia"
    __params__ = "nada"
    __returns__ ="dia"
    __descriptions__ = "Este metodo permite conocer el dia"
    def DarDia(self):
        # aqui va mi codigo
        return self.dia
    
    __method__ = "CambiarDia"
    __params__ = "nuevoDia"
    __returns__ ="nada"
    __descriptions__ = "Este metodo permite cambiar el dia"
    def CambiarDia(self, nuevoDia):
        # aqui va mi codigo
        self.dia = nuevoDia
    
    __method__ = "DarMes"
    __params__ = "nada"
    __returns__ ="nada"
    __descriptions__ = "Este metodo permite conocer el mes"    
    def DarMes(self):
        # aqui va mi codigo
        return self.mes
    
    __method__ = "CambiarMes"
    __params__ = "nuevoMes"
    __returns__ ="nada"
    __descriptions__ = "Este metodo permite retirnar el mes"  
    def CambiarMes(self, nuevoMes):
        # aqui va mi codigo
        self.mes = nuevoMes
    
    __method__ = "DarAnio"
    __params__ = "nada"
    __returns__ ="anio"
    __descriptions__ = "Este metodo permite conocer el anio"   
    def DarAnio(self):
        # aqui va mi codigo
        return self.anio
    
    __method__ = "CambiarAnio"
    __params__ = "nuevoanio"
    __returns__ ="nada"
    __descriptions__ = "Este metodo permite cambiar el anio"   
    def CambiarAnio(self, nuevoAnio):
        # aqui va mi codigo
        self.anio = nuevoAnio
        
    __method__ = "DarFecha"
    __params__ = "Ninguno"
    __returns__ = "Fecha"
    __descriptions__ = "Metodo que retorna la fecha"
    def DarFecha(self):
        return f'{self.DarDia()}/{self.DarMes()}/{self.DarAnio()}'