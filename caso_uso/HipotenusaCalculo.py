#
#Classe responsável por calcular a hipotenusa
#
import numpy as np

class HipotenusaCalculo:
    
    def calculate(self, cateto_oposto, cateto_adjacente):
        return np.sqrt(np.power(cateto_oposto, 2) + np.power(cateto_adjacente, 2))