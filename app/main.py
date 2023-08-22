from app.Battle.fight import fight
from app.knights.create_knight import CreateKnight
from app.knights.knight_prep import knight_preparation


def battle(knights: dict) -> dict:
    lancelot = CreateKnight(
        knights["lancelot"]["name"],
        knights["lancelot"]["power"],
        knights["lancelot"]["hp"]
    )
    arthur = CreateKnight(
        knights["arthur"]["name"],
        knights["arthur"]["power"],
        knights["arthur"]["hp"]
    )
    mordred = CreateKnight(
        knights["mordred"]["name"],
        knights["mordred"]["power"],
        knights["mordred"]["hp"]
    )
    red_knight = CreateKnight(
        knights["red_knight"]["name"],
        knights["red_knight"]["power"],
        knights["red_knight"]["hp"]
    )

    list_of_knights = [lancelot, arthur, mordred, red_knight]

    knight_preparation(list_of_knights, knights)

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        "Arthur": arthur.hp,
        "Lancelot": lancelot.hp,
        "Mordred": mordred.hp,
        "Red Knight": red_knight.hp
    }
