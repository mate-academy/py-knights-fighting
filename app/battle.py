from typing import Dict, Any
from app.knights import Knight


def fight(knight1: Knight, knight2: Knight) -> None:
    """Провести бій між двома лицарами.

    Args:
        knight1: Перший учасник бою
        knight2: Другий учасник бою
    """
    damage_to_knight1 = max(0, knight2.power - knight1.protection)
    damage_to_knight2 = max(0, knight1.power - knight2.protection)

    knight1.take_damage(damage_to_knight1)
    knight2.take_damage(damage_to_knight2)


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    """Провести турнір між усіма лицарами.

    Args:
        knights_config: Словник з конфігурацією всіх лицарів

    Returns:
        Словник з результатами боїв (ім'я лицаря та залишок здоров'я)
    """
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
