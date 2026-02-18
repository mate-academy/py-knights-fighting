from typing import Dict
from app.models import Knight


def battle(knightsconfig: Dict[str, Dict]) -> Dict[str, int]:
    # Створюємо список об'єктів Knight
    fighters = [Knight(**knightsconfig[name]) for name in
                ["lancelot", "arthur", "mordred", "red_knight"]]

    # Підготовка до бою
    for knight in fighters:
        knight.prepare_for_battle()

    # Розподіл боїв
    lancelot, arthur, mordred, red_knight = fighters

    # 1. Lancelot vs Mordred
    lancelot.take_damage(mordred.power - lancelot.protection)
    mordred.take_damage(lancelot.power - mordred.protection)

    # 2. Arthur vs Red Knight
    arthur.take_damage(red_knight.power - arthur.protection)
    red_knight.take_damage(arthur.power - red_knight.protection)

    # Збір результатів
    results: Dict[str, int] = {}
    for knight in fighters:
        results.update(knight.battle_results())

    return results
