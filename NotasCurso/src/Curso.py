__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

class Curso:
    
    ######################################################
    # Constantes
    ######################################################
    
    TOTAL_EST = 12
    
    def __init__(self):
        self.notas = []
    
    def NoHaceNada(self, valor):
        indice = 10
        self.notas[0] = 3.5
        
        if valor < 2.5 and len(self.notas) == self.TOTAL_EST:
            self.notas[indice] = self.notas[0]
            self.notas[0]=valor + 1
        else:
            self.notas[indice] = self.notas[0] - valor
            