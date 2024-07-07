from app.knight import Knight
from app.knights_config import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {
        name: Knight.from_dict(data)
        for name, data in knights_config.items()
    }
    for knight in knights.values():
        knight.use_power_ups()

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
