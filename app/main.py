from app.battle.fight import fight
from app.characters.knight import Knight
from app.characters.utils import prepare_knights


def battle(knights: dict) -> dict:
    lancelot = Knight(
        knights["lancelot"]["name"],
        knights["lancelot"]["power"],
        knights["lancelot"]["hp"]
    )
    arthur = Knight(
        knights["arthur"]["name"],
        knights["arthur"]["power"],
        knights["arthur"]["hp"]
    )
    mordred = Knight(
        knights["mordred"]["name"],
        knights["mordred"]["power"],
        knights["mordred"]["hp"]
    )
    red_knight = Knight(
        knights["red_knight"]["name"],
        knights["red_knight"]["power"],
        knights["red_knight"]["hp"]
    )

    list_of_knights = [lancelot, arthur, mordred, red_knight]

    prepare_knights(list_of_knights, knights)

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        "Arthur": arthur.hp,
        "Lancelot": lancelot.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp
    }
