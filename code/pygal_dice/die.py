from random import randint


class Die:
    """A class, that represents one dice"""

    def __init__(self, num_sides=6):
        """6-side dice by default"""
        self.num_sides = num_sides

    def roll(self):
        """"Return random number from 1 to dice sides count"""
        return randint(1, self.num_sides)
