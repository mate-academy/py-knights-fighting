from random import randint


def rolling():
    first_dice = randint(1, 5)
    second_dice = randint(1, 5)
    modifier = 1 + (first_dice + second_dice) / 10
    return modifier


def modifying(a, b):
    return a * b
