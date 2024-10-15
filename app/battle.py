from app.knight import Knight
from typing import Dict


def fight(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= max(0, knight2.power - knight1.armour.protection)
    knight2.hp -= max(0, knight1.power - knight2.armour.protection)
    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)


def battle(knights_config: Dict[str, Dict]) -> Dict[str, int]:
    lancelot = Knight(knights_config["lancelot"])
    arthur = Knight(knights_config["arthur"])
    mordred = Knight(knights_config["mordred"])
    red_knight = Knight(knights_config["red_knight"])

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
