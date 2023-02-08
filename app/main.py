import time
from random import randint

from app.king_garden.knights import Knight
from app.armory.squire import Squire
from app.arena.duel import duel

from app.king_garden.raw_data import KNIGHTS_DATA


def battle(knights_old: dict[str | dict]) -> dict[str]:
    knights = {
        knight: Knight(name=data["name"], power=data["power"], hp=data["hp"])
        for knight, data in knights_old.items()
    }
    squire = Squire("Alyosha")
    squire.take_arms_from(knights_old)
    time.sleep(randint(1, 3))

    squire.knights_enarm(
        [(name, knight) for name, knight in zip(knights_old.keys(),
                                                (knights.values()))]
    )
    time.sleep(randint(1, 3))

    for name, knight in zip(knights_old.keys(), knights.values()):
        knight.take_and_drink_potion(name, knights_old)
    time.sleep(randint(1, 3))

    print("Round one: Lancelot VS Mordred")

    duel(knights["lancelot"], knights["mordred"])
    print("Cleaners clearing, jit jeating, fit fitting")
    time.sleep(randint(5, 8))

    print("Round two: Arthur VS Red Knight")

    duel(knights["arthur"], knights["red_knight"])
    return {knight.name: knight.hp for knight in knights.values()}


battle(KNIGHTS_DATA)  # second uncomment in case You want to play with it
