"""Class that represents a Die"""

from random import randint

class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides;

    def roll_die(self) -> int:
        return randint(1, self.sides)
