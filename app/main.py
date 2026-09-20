from app.models.knight import Knight
from app.battle.mechanics import Battle


def battle(knights: dict) -> dict:
    """Execute battle rounds and return hp results."""
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight(
        name=knights["lancelot"]["name"],
        power=knights["lancelot"]["power"],
        hp=knights["lancelot"]["hp"],
        armour=knights["lancelot"]["armour"],
        weapon=knights["lancelot"]["weapon"],
        potion=knights["lancelot"]["potion"],
    )
    lancelot.prepare()

    # arthur
    arthur = Knight(
        name=knights["arthur"]["name"],
        power=knights["arthur"]["power"],
        hp=knights["arthur"]["hp"],
        armour=knights["arthur"]["armour"],
        weapon=knights["arthur"]["weapon"],
        potion=knights["arthur"]["potion"],
    )
    arthur.prepare()

    # mordred
    mordred = Knight(
        name=knights["mordred"]["name"],
        power=knights["mordred"]["power"],
        hp=knights["mordred"]["hp"],
        armour=knights["mordred"]["armour"],
        weapon=knights["mordred"]["weapon"],
        potion=knights["mordred"]["potion"],
    )
    mordred.prepare()

    # red_knight
    red_knight = Knight(
        name=knights["red_knight"]["name"],
        power=knights["red_knight"]["power"],
        hp=knights["red_knight"]["hp"],
        armour=knights["red_knight"]["armour"],
        weapon=knights["red_knight"]["weapon"],
        potion=knights["red_knight"]["potion"],
    )
    red_knight.prepare()

    # ---------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    round_1 = Battle(lancelot, mordred)
    round_1.fight()

    # 2 Arthur vs Red Knight:
    round_2 = Battle(arthur, red_knight)
    round_2.fight()

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
