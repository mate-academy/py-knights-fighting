from app.knight.config import KNIGHTS
from app.knight.stats import Knight


def battle(knights_config: dict) -> dict:

    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    knights_list = [lancelot, arthur, mordred, red_knight]
    battle_result = {}

    for element in knights_list:
        element.knight_protection()
        element.knight_weapon()
        element.knight_potion()

    lancelot.battle(mordred)
    arthur.battle(red_knight)

    for element in knights_list:
        battle_result.update(element.knight_final_stats())

    return battle_result


print(battle(KNIGHTS))
