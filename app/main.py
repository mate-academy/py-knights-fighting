from app.knights import Knight
from app.battle import battle_result
from app.knights_dict import KNIGHTS


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])
    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    battle_result(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    battle_result(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
