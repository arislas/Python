"""Devuelve datos sobre un sorteo de loetería."""

import loteria

sorteo = loteria.Loteria((2,5,3,1,4))

print(f"\nMi número es: {sorteo.mi_num()}")
sorteo.comprueba_numero()