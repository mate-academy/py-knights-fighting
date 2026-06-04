from app.constants import KNIGHTS
from app.knight import KnightConfig
from app.battle import fight


def battle(knights_config: dict) -> dict:
    knights = {}
    for knight_name, knight_value in knights_config.items():
        knights[knight_name] = KnightConfig(knight_value)

    lancelot = knights["lancelot"]
    arthur = knights["arthur"]
    mordred = knights["mordred"]
    red_knight = knights["red_knight"]

    fight(lancelot, mordred)
    fight(red_knight, arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
