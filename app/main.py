from app.battle_preparation import Knight
from app.config import KNIGHTS


def fight(knight1: Knight, knight2: Knight) -> dict:
    knight2.hp -= knight1.power - knight2.protection
    knight1.hp -= knight2.power - knight1.protection

    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }


def battle(config: dict) -> dict:
    lancelot = Knight(config["lancelot"])
    mordred = Knight(config["mordred"])
    arthur = Knight(config["arthur"])
    red_knight = Knight(config["red_knight"])

    return {
        **fight(lancelot, mordred),
        **fight(arthur, red_knight),
    }


print(battle(KNIGHTS))
