#
#Classe responsável por calcular o cateto adjacente
#

import numpy as np

class CatetoAdjacenteCalculo :
   
    def calculate(self, hipotenusa, cateto_oposto):
        return np.sqrt(np.power(hipotenusa, 2) - np.power(cateto_oposto, 2))