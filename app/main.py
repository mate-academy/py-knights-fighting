from app.knights.knight import Knight
from app.knights.knights_data import KNIGHTS
from app.battle.fight import Fight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS:

    # lancelot
    lancelot = Knight.create_knight(knights_config["lancelot"])
    lancelot.prepare_to_battle()

    # arthur
    arthur = Knight.create_knight(knights_config["arthur"])
    arthur.prepare_to_battle()

    # mordred
    mordred = Knight.create_knight(knights_config["mordred"])
    mordred.prepare_to_battle()

    # red_knight
    red_knight = Knight.create_knight(knights_config["red_knight"])
    red_knight.prepare_to_battle()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    Fight.fight(lancelot, mordred)

    # 2 Arthur vs Red Knight:
    Fight.fight(arthur, red_knight)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
