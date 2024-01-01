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
        """Devuelve un string con el número comprado."""
        self.num_comprado_str = ''
        for num in self.num_comprado:
            self.num_comprado_str += str(num)
        return self.num_comprado_str
    
    def genera_numero(self):
        """Genera un número de 5 cifras y lo devuelve como string."""
        n = 0
        lista = []
        
        while(n < 5):
            lista.append(self.numeros[randint(0, len(self.numeros) - 1)])
            n += 1
        
        cadena = ''.join(map(str, lista))
        return cadena

    def comprueba_numero(self):
        """
        Simula el sorteo y compara el numero premiado con el nuestro.
        Devuelve True si son iguales.
        """
        sorteo = self.genera_numero()
        #print(f"\n{self.mi_num()} == {sorteo} -> {self.mi_num == sorteo}\n")
        if self.mi_num() == sorteo:
            return (True, sorteo, self.mi_num())
        else:
            return (False, sorteo, self.mi_num())
    
    def n_sorteos(self, n):
        """Hace n sorteos y comprueba los resultados con nuestro número."""
        realizados = 0
        
        while realizados < n:
            self.comprueba_numero()
            realizados += 1
    
    def juega_hasta_acertar(self):
        """saca números hasta que acierta con el nuestro."""
        intentos = 0
        
        while True:
            intentos += 1
            resultado = self.comprueba_numero()
            if resultado[0]:
                print(f"\n{resultado[2]} == {resultado[1]} -> {resultado[2] == resultado[1]}\n")
                print(f"\nHas necesitado {intentos} intentos para acertar.\n")
                return intentos
                break
            else:
                print(f"\n{resultado[2]} == {resultado[1]} -> {resultado[2] == resultado[1]}\n")
    
    def media_intentos(self, n):
        """Devuelve la media para acertar de n sorteos."""
        sorteos = 0
        resultados = []

        while(sorteos < n):
            resultados.append(self.juega_hasta_acertar())
            sorteos += 1
        
        total = 0
        
        for resultado in resultados:
            total += resultado
        
        print(resultados)
        return total / len(resultados)