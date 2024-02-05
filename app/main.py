from app.stats import KNIGHTS
from app.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])
    # BATTLE:
    lancelot.hp, mordred.hp = fight(lancelot, mordred)
    arthur.hp, red_knight.hp = fight(arthur, red_knight)
    # Return battle results:
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }


def fight(fighter_1: Knight, fighter_2: Knight) -> tuple:
    fighter_1.hp -= fighter_2.power - fighter_1.protection
    fighter_2.hp -= fighter_1.power - fighter_2.protection
    return max(fighter_1.hp, 0), max(fighter_2.hp, 0)


print(battle(KNIGHTS))
