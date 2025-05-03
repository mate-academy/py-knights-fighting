from app.battle.battle import Battle
from app.preparation.knight import Knight
from app.preparation.knight_config import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.prepare_knight(knights_config["lancelot"])

    # arthur
    arthur = Knight.prepare_knight(knights_config["arthur"])

    # mordred
    mordred = Knight.prepare_knight(knights_config["mordred"])

    # red_knight
    red_knight = Knight.prepare_knight(knights_config["red_knight"])

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Battle(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    Battle(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
