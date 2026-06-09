from app.data.knights import KNIGHTS
from app.logic.battle import fight
from app.logic.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(
        knights_config["lancelot"]
    )

    arthur = Knight(
        knights_config["arthur"]
    )

    mordred = Knight(
        knights_config["mordred"]
    )

    red_knight = Knight(
        knights_config["red_knight"]
    )

    fight(lancelot, mordred)

    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
