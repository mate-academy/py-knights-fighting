from app.knight import Knight
from app.battle import fight
from app.knights_dict import KNIGHTS


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.apply_stats()
    arthur.apply_stats()
    mordred.apply_stats()
    red_knight.apply_stats()

    lancelot, mordred = fight(lancelot, mordred)
    arthur, red_knight = fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


print(battle(KNIGHTS))
