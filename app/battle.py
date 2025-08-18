from typing import Dict, Any
from app.models.knight import Knight


def duel(knight1: Knight, knight2: Knight) -> None:
    knight1.take_damage(knight2.power - knight1.protection)
    knight2.take_damage(knight1.power - knight2.protection)


def battle(knightsConfig: Dict[str, Any]) -> Dict[str, int]:
    lancelot = Knight(knightsConfig["lancelot"])
    arthur = Knight(knightsConfig["arthur"])
    mordred = Knight(knightsConfig["mordred"])
    red_knight = Knight(knightsConfig["red_knight"])

    duel(lancelot, mordred)
    duel(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
