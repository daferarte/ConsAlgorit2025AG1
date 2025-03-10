__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

################################################################
# importaciones
################################################################

from Fecha import Fecha

class Empleado:
    #Aqui va mi codigo
    nombre = ''
    apellido = ''
    # 1=Masculino, 2=Femenino
    sexo=0
    salario = 0
    # Fechas asociaciones
    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()
    
    ################################################################
    # Constructor
    ################################################################
    
    def __init__(self, nombre, apellido, sexo, salario):
        # aqui va mi codigo
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.salario = salario
    
    ################################################################
    # Metodos
    ################################################################
    __method__ = "Cambiar Salario"
    __params__ = "nuevoSalario"
    __returns__ ="nada"
    __descriptions__ = "Este metodo permite cambiar el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        # aqui va mi codigo
        self.salario=nuevoSalario
    
    __method__ = "DuplicarSalario"
    __params__ = "nada"
    __returns__ ="nada"
    __descriptions__ = "Este metodo permite duplicar el salario del empleado"    
    def DuplicarSalario(self):
        # aqui va mi codigo
        self.salario = self.salario * 2
    
    __method__ = "CalcularSalarioAnual"
    __params__ = "nada"
    __returns__ ="Salario anual del empleado"
    __descriptions__ = "Este metodo permite calcular y retornar el salario del empleado"
    def CalcularSalarioAnual(self):
        # aqui va mi codigo
        return self.salario * 12
    
    __method__ = "DarSalario"
    __params__ = "nada"
    __returns__ ="Salario"
    __descriptions__ = "Este metodo permite conocer el salario que tiene un empleado"
    def DarSalario(self):
        # aqui va mi codigo
        return self.salario
    
    __method__ = "CalcularImpuestos"
    __params__ = "nada"
    __returns__ ="Impuestos anuales"
    __descriptions__ = "Este metodo permite conocer los impuestos anuales que tiene un empleado"
    def CalcularImpuestos(self):
        # aqui va mi codigo
        salarioAnual = self.CalcularSalarioAnual()
        return salarioAnual * 19.5 / 100
    
    ################################################################
    # llamada a metodos
    ################################################################
    
    __method__ = "DarDiaIngreso"
    __params__ = "nada"
    __returns__ ="Dia Ingreso"
    __descriptions__ = "Este metodo permite conocer el dia de ingreso de un empleado"
    def DarDiaIngreso(self):
        # aqui va mi codigo
        return self.fechaIngreso.DarDia()
    
    __method__ = "CambiarFechaIngreso"
    __params__ = "dia, mes, anio"
    __returns__ = "ninguno"
    __descriptions__ = "Metodo que permite cambiar la fecha de ingreso a la empresa del empleado"
    def CambiarFechaIngreso(self, dia, mes, anio):
        self.fechaIngreso.CambiarDia(dia)
        self.fechaIngreso.CambiarMes(mes)
        self.fechaIngreso.CambiarAnio(anio)
        
    __method__ = "CambiarFechaNacimiento"
    __params__ = "dia, mes, anio"
    __returns__ = "ninguno"
    __descriptions__ = "Metodo que permite cambiar la fecha de nacimiento del empleado"
    def CambiarFechaNacimiento(self, dia, mes, anio):
        self.fechaNacimiento.CambiarDia(dia)
        self.fechaNacimiento.CambiarMes(mes)
        self.fechaNacimiento.CambiarAnio(anio)
    
    __method__ = "DarFechaIngreso"
    __params__ = "Ninguno"
    __returns__ = "fechaIngreso"
    __descriptions__ = "Metodo que retorna la fecha de ingreso a la empresa del empleado"
    def DarFechaIngreso(self):
        # Aqui va el codigo
        # forma 1
        fechaIngreso = f'{self.fechaIngreso.DarDia()}/{self.fechaIngreso.DarMes()}/{self.fechaIngreso.DarAnio()}'
        return fechaIngreso
    
        # forma 2
        return f'{self.fechaIngreso.DarDia()}/{self.fechaIngreso.DarMes()}/{self.fechaIngreso.DarAnio()}'
    
    
    __method__ = "DarFechaNacimiento"
    __params__ = "Ninguno"
    __returns__ = "fechaNacimiento"
    __descriptions__ = "Metodo que retorna la fecha de nacimiento del empleado"
    def DarFechaNacimiento(self):
        # Aqui va el codigo
        # forma 1
        fechaNacimiento = f'{self.fechaNacimiento.DarDia()}/{self.fechaNacimiento.DarMes()}/{self.fechaNacimiento.DarAnio()}'
        return fechaNacimiento
    
        # forma 2
        return f'{self.fechaNacimiento.DarDia()}/{self.fechaNacimiento.DarMes()}/{self.fechaNacimiento.DarAnio()}'