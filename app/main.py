from app.data.knights import KNIGHTS
from app.knight.knight import Knight


def battle(knights_config: dict) -> dict:
    knights = [Knight(**knight) for knight in knights_config.values()]
    lancelot, arthur, mordred, red_knight = knights

    # BATTLE PREPARATIONS

    for knight in knights:
        knight.battle_preparation()

    # BATTLE:

    # 1 Lancelot vs Mordred and check if someone fell in battle:
    lancelot.duelling(mordred)

    # 2 Arthur vs Red Knight and check if someone fell in battle:
    arthur.duelling(red_knight)

    # Return battle results:
    return {knight.name: knight.hp for knight in knights}


print(battle(KNIGHTS))
