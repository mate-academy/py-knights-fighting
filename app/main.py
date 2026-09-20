from app.models.knight import Knight
from app.battle.mechanics import Battle


def battle(knights: dict) -> dict:
    """Execute battle rounds and return hp results."""
    # BATTLE PREPARATIONS:

    prepared_knights = {}
    knight_keys = ["lancelot", "arthur", "mordred", "red_knight"]

    for knight_key in knight_keys:
        config = knights[knight_key]
        knight = Knight(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config["armour"],
            weapon=config["weapon"],
            potion=config["potion"],
        )
        knight.prepare()
        prepared_knights[knight_key] = knight

    lancelot = prepared_knights["lancelot"]
    arthur = prepared_knights["arthur"]
    mordred = prepared_knights["mordred"]
    red_knight = prepared_knights["red_knight"]

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
