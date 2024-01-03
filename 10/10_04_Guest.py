# Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
from pathlib import Path

path = Path('10/guest.txt')

name = input('¿Cuál es tu nombre? ')

path.write_text(name)