#
#Classe responsável por calcular o cateto oposto
#
import numpy as np

class CatetoOpostoCalculo :
    
    def calculate(self, hipotenusa, cateto_adjacente):
        return np.sqrt(np.power(hipotenusa, 2) - np.power(cateto_adjacente, 2))

