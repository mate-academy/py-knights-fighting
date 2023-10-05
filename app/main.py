from app.characters.data import KNIGHTS

from app.characters.knights import Character
from app.competitions.fight import fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Character(knights_config["lancelot"])
    arthur = Character(knights_config["arthur"])
    mordred = Character(knights_config["mordred"])
    red_knight = Character(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
