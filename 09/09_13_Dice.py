"""Simple atmpt to made a die with 6 sides."""
from random import randint

class Die:
    def __init__(self):
        """Initialize sides."""
        self.sides = 6
    
    def roll_die(self):
        return(randint(1, self.sides))

sided = Die()

n = 1
while n <= 10:
    if n < 10:
        print(f"Esta es la tirada 0{n}: {sided.roll_die()}")
        n += 1
    else:
        print(f"Esta es la tirada {n}: {sided.roll_die()}")
        n += 1