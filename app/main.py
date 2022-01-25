from app.knight.knight import Knight
from app.data.knight_data import KNIGHTS


def battle(knights_config):
    lancelot = Knight.create_knight(knights_config["lancelot"])
    arthur = Knight.create_knight(knights_config["arthur"])
    mordred = Knight.create_knight(knights_config["mordred"])
    red_knight = Knight.create_knight(knights_config["red_knight"])

    lancelot.battle(mordred)

    arthur.battle(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
