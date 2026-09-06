from app.models.knight import Knight
from app.config.knights import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = [
        Knight(knights_config["lancelot"]),
        Knight(knights_config["arthur"]),
        Knight(knights_config["mordred"]),
        Knight(knights_config["red_knight"])
    ]

    for knight in knights:
        knight.prepare_for_battle()

    lancelot, arthur, mordred, red_knight = knights

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        knight.name: knight.hp
        for knight in knights
    }


if __name__ == "__main__":
    print(battle(KNIGHTS))
