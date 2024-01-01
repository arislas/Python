import time
from random import randint

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
my_ticket = [2, 1, 6, 7, 3]
my_ticket_str = ''

for number in my_ticket: # Convierte my_ticket en una cadena
    my_ticket_str += str(number)

print(f"\nMy number is: {my_ticket_str}.\n")

attempts = 0
start_time = time.time()  # Registra el tiempo de inicio

while True: # Bucle que no se rompe hasta acertar el número
    n = 0
    winner = []
    while n < 5: # Genera números aleatorios de 5 cifras de la tupla numbers y los guarda en winner
        winner.append(numbers[randint(0, len(numbers) - 1)])
        n += 1
    
    attempts += 1

    winner_str = ''.join(map(str, winner)) # Guarda el número de la lista winner como una cadena sin espacios
    print(f"{winner_str}", end = '\t')  # Imprime el número ganador sin espacios separados por un tabulador

    if (attempts % 13) == 0: # Cambia de líena cada 13 números
        print("\n")

    if winner == my_ticket:
        end_time = time.time()  # Registra el tiempo de finalización
        elapsed_time = end_time - start_time  # Calcula el tiempo transcurrido
        print(f"\n\nYou needed {attempts} attempts to win the lottery with number {my_ticket_str}.")
        print(f"Time elapsed: {elapsed_time} seconds.\n")
        gasto = 20 * attempts
        print(f"Para ganar el premio deberías haber gastado: {gasto} euros.\n")
        break
