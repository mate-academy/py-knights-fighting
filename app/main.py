from app.data.knights import KNIGHTS
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    # BATTLE PREPARATIONS

    lancelot = Knight(knights_config["lancelot"])
    lancelot.battle_preparation()

    arthur = Knight(knights_config["arthur"])
    arthur.battle_preparation()

    mordred = Knight(knights_config["mordred"])
    mordred.battle_preparation()

    red_knight = Knight(knights_config["red_knight"])
    red_knight.battle_preparation()

    # -------------------------------------------------------------------------------
    # BATTLE:

    # 1 Lancelot vs Mordred:
    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    # check if someone fell in battle
    lancelot.fell_in_battle()
    mordred.fell_in_battle()

    # 2 Arthur vs Red Knight:
    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    # check if someone fell in battle
    arthur.fell_in_battle()
    red_knight.fell_in_battle()

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
