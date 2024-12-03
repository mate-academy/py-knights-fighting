from app.Knight.Knight import Knight
from app.Knight.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    lancelot.prepare_to_battle()
    arthur.prepare_to_battle()
    mordred.prepare_to_battle()
    red_knight.prepare_to_battle()

    lancelot.fight(mordred.power)
    mordred.fight(lancelot.power)
    arthur.fight(red_knight.power)
    red_knight.fight(arthur.power)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
