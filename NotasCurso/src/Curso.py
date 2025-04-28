__author__ = "Daniel Fernando Arteaga"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "daniel.arteagafajar@campusucc.edu.co"

import random
class Curso:
    
    ######################################################
    # Constantes
    ######################################################
    
    TOTAL_EST = 12
    
    def __init__(self):
        self.notas = []
        self.LlenarNotas()
    
    def LlenarNotas(self):
        est_Cont=0
        while est_Cont < self.TOTAL_EST:
            self.notas[est_Cont]= random.uniform(1.0, 5.0)
            est_Cont +=1
    
    
    def PromedioNotas(self):
        # suma:float = self.notas[0]
        # suma += self.notas[1]
        # suma += self.notas[2]
        # suma += self.notas[3]
        # suma += self.notas[4]
        # suma += self.notas[5]
        # suma += self.notas[6]
        # suma += self.notas[7]
        # suma += self.notas[8]
        # suma += self.notas[9]
        # suma += self.notas[10]
        # suma += self.notas[11]
        
        # suma =0
        # est = 0
        
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        # suma += self.notas[est]
        # est += 1
        
        suma =0
        est = 0
        
        while est < self.TOTAL_EST:
            suma += self.notas[est]
            est += 1
        
        return suma/self.TOTAL_EST

    def PromedioNotasFor(self):
        
        suma = 0
        for nota in self.notas:
            suma += nota
        
        return suma/self.TOTAL_EST
    
    def NoHaceNada(self, valor):
        indice = 10
        self.notas[0] = 3.5
        
        if valor < 2.5 and len(self.notas) == self.TOTAL_EST:
            self.notas[indice] = self.notas[0]
            self.notas[0]=valor + 1
        else:
            self.notas[indice] = self.notas[0] - valor
            