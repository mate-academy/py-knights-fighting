from app.classes.Knights import Knight
from app.classes.Battle import Battle
from app.data.knights import KNIGHTS as kn


def createKnight(knights):
    knigths_dict = {}
    for key in knights:
        knight_info = knights[key]
        knight = Knight(
            name=knight_info["name"],
            power=knight_info["power"],
            hp=knight_info["hp"],
            armour=knight_info["armour"],
            weapon=knight_info["weapon"],
            potion=knight_info["potion"],
        )
        knigths_dict[key] = knight
    return knigths_dict

    # -------------------------------------------------------------------------------
    # BATTLE:


def battle(knightsConfig) -> dict:
    # BATTLE PREPARATIONS:

    knights = createKnight(knightsConfig)

    battle1 = Battle(knights["lancelot"], knights["mordred"])
    battle2 = Battle(knights["arthur"], knights["red_knight"])

    result1 = battle1.start_battle()
    result2 = battle2.start_battle()

    return {
        "Lancelot": result1["Lancelot"],
        "Arthur": result2["Arthur"],
        "Mordred": result1["Mordred"],
        "Red Knight": result2["Red Knight"],
    }


print(battle(kn))
