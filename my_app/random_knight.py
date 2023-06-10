from random import randint

from app.knight import Knight


def random_knight() -> Knight:
    """
    This function creates instance of Knight class with random
    characteristics.
    """
    name = input("Input name of You knight, please: ")
    power = randint(0, 100)
    hp = randint(0, 100)
    protection = randint(0, 100)
    return Knight(
        name=name,
        power=power,
        hp=hp,
        protection=protection
    )
