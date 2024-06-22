from tournament.service import create_knights
from tournament.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = create_knights(knights_config)

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    lancelot.fight(mordred)

    arthur = knights["arthur"]
    red_knight = knights["red_knight"]
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
