"""Devuelve datos sobre un sorteo de loetería."""

import loteria

sorteo = loteria.Loteria((2,5,3,1,4))

print(f"\nMi número es: {sorteo.mi_num()}")

n = 200
media = sorteo.media_intentos(n)

print(f"\nLa media de intentos de {n} sorteos es: {media}\n")
coste = 20 * media
print(f"El coste medio para acertar el número es {coste} €.\n")