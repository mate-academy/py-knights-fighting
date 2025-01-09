from app.data.knights import KNIGHTS
from app.knight.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = lancelot, arthur, mordred, red_knight = [
        Knight(**knight)
        for knight
        in knights_config.values()
    ]

    # BATTLE PREPARATIONS

    for knight in knights:
        knight.battle_preparation()

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
    return {knight.name: knight.hp for knight in knights}


battle(KNIGHTS)
