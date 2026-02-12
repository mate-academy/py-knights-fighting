from preparations.knights_configs import KNIGHTS
from preparations.knights import Knight


def battle(knights_config: dict) -> dict:
    knights = [
        Knight(config).prepare_for_battle()
        for config in knights_config.values()
    ]
    lancelot, arthur, mordred, red_knight = knights

    # 1 Lancelot vs Mordred:
    lancelot.attack(mordred)
    mordred.attack(lancelot)

    # 2 Arthur vs Red Knight:
    arthur.attack(red_knight)
    red_knight.attack(arthur)

    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


if "__main__" == __name__:
    knights_config = KNIGHTS
