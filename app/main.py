from app.king_garden.knights import Knight
from app.armory.squire import Squire
from app.arena.duel import duel


def battle(knights_old: dict[str | dict]) -> dict[str]:
    knights = {
        knight: Knight(name=data["name"], power=data["power"], hp=data["hp"])
        for knight, data in knights_old.items()
    }
    squire = Squire("Alyosha")
    squire.take_arms_from(knights_old)

    squire.knights_enarm(
        [(name, knight) for name, knight in zip(knights_old.keys(),
                                                (knights.values()))]
    )

    for name, knight in zip(knights_old.keys(), knights.values()):
        knight.take_and_drink_potion(name, knights_old)

    print("Round one: Lancelot VS Mordred")

    duel(knights["lancelot"], knights["mordred"])
    print("Cleaners clearing, jit jeating, fit fitting")

    print("Round two: Arthur VS Red Knight")

    duel(knights["arthur"], knights["red_knight"])
    return {knight.name: knight.hp for knight in knights.values()}
