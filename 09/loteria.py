"""Modulo que simula un sorteo de lotería nacional."""

import time
from random import randint

class Loteria:
    """Simula un sorteo de lotería nacional."""

    def __init__(self, num_comprado = (2,1,6,7,3)):
        self.numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.num_comprado = num_comprado
        self.num_comprado_str = ''

    def mi_num(self):
        """Devuelve una cadena con el número comprado."""
        self.num_comprado_str = ''
        for num in self.num_comprado:
            self.num_comprado_str += str(num)
        return self.num_comprado_str
    
    def genera_numero(self):
        """Genera un número de 5 cifras."""
        n = 0
        lista = []
        
        while(n < 5):
            lista.append(self.numeros[randint(0, len(self.numeros) - 1)])
            n += 1
        
        cadena = ''.join(map(str, lista))
        return cadena

    def comprueba_numero(self):
        sorteo = self.genera_numero()
        print(f"\n{self.mi_num()} == {sorteo} -> {self.mi_num == sorteo}\n")
        if self.mi_num() == self.genera_numero():
            return True
        else:
            return False