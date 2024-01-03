# Write a while loop that prompts users for their name. Collect
# all the names that are entered, and then write these names to a file called
# guest_book.txt. Make sure each entry appears on a new line in the file.

from pathlib import Path

lista = []

while True:
    nombre = input('Escribe tu nombre, "q" para acabar: ')
    if nombre == 'q':
        break
    else:
        lista.append(nombre)

contenido = ''
path = Path('10/guest_book.txt')

for nombre in lista:
    contenido += nombre + "\n"

path.write_text(contenido)