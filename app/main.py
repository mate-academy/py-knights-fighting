from app.characters.data import KNIGHTS

from app.characters.knights import Character
from app.competitions.fight import fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    knights = {
        "lancelot": Character(knights_config["lancelot"]),
        "arthur": Character(knights_config["arthur"]),
        "mordred": Character(knights_config["mordred"]),
        "red_knight": Character(knights_config["red_knight"])
    }

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(knights["lancelot"], knights["mordred"])

    # 2 Arthur vs Red Knight:
    fight(knights["arthur"], knights["red_knight"])

    # Return battle results:
    return {
        knight.name: knight.hp for knight in knights.values()
    }


print(battle(KNIGHTS))
