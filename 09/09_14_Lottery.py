"""A simple attemp to model a lottery game."""
from random import randint

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E')
winner = []

n = 0
while n < 4:
    winner.append(numbers[randint(0, len(numbers) - 1)])
    n += 1

print("\nThe winner ticket is:")

for number in winner:
    print(number, end = '')

print("\n")