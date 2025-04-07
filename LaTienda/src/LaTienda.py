__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

from Tipo import Tipo
from Producto import Producto

class Tienda:
    
    def __init__(self):
        self.producto1 = Producto("Lazpiz", Tipo.PAPELERIA, 550.0, 10, 'A', 5)
        self.producto2 = Producto("Aspirina", Tipo.FARMACIA, 109.5, 25, 'A', 8)
        self.producto3 = Producto("Borrador", Tipo.PAPELERIA, 207.3, 30, 'A', 10)
        self.producto4 = Producto("Pan", Tipo.SUPERMERCADO, 150.0, 15, 'A', 20)
        self.dineroCaja = 0
        
    
    