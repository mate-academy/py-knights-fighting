from app.knight import Knight
from app.knights_setup import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight.from_dict(knights_config["lancelot"])
    lancelot.get_ready_to_battle()

    arthur = Knight.from_dict(knights_config["arthur"])
    arthur.get_ready_to_battle()

    mordred = Knight.from_dict(knights_config["mordred"])
    mordred.get_ready_to_battle()

    red_knight = Knight.from_dict(knights_config["red_knight"])
    red_knight.get_ready_to_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Knight.fight_knight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    Knight.fight_knight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
