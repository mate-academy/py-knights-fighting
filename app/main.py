from app.input import KNIGHTS
from app.fight import fight


def battle(knights_config: dict) -> dict:

    knight_instances = fight(knights_config)

    lancelot = knight_instances[0]
    mordred = knight_instances[2]
    lancelot - mordred
    mordred - lancelot

    arthur = knight_instances[1]
    red_knight = knight_instances[3]
    arthur - red_knight
    red_knight - arthur

    return {
        lancelot.name: max(lancelot.hp, 0),
        arthur.name: max(arthur.hp, 0),
        mordred.name: max(mordred.hp, 0),
        red_knight.name: max(red_knight.hp, 0),
    }


print(battle(KNIGHTS))
