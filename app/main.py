from app.knight import Knight
from app.knights_data import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot.prepare_for_battle()
    arthur.prepare_for_battle()
    mordred.prepare_for_battle()
    red_knight.prepare_for_battle()

    lancelot.take_damage(mordred.power)
    mordred.take_damage(lancelot.power)

    arthur.take_damage(red_knight.power)
    red_knight.take_damage(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
