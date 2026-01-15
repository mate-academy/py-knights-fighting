from app.knights.cls_knight import Knight
from app.knights.knights import KNIGHTS


def knights_fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config: dict) -> dict:
    knights = {
        attribute: Knight(*value.values())
        for attribute, value in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare_for_battle()

    knights_fight(knights["lancelot"], knights["mordred"])
    knights_fight(knights["arthur"], knights["red_knight"])

    return {knight.name: knight.hp for knight in knights.values()}


print(battle(KNIGHTS))
