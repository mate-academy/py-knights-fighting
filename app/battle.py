from typing import Dict, Any
from .knight import Knight


def fight(knight_1: Knight, knight_2: Knight) -> None:
    damage_to_1 = knight_2.power - knight_1.protection
    damage_to_2 = knight_1.power - knight_2.protection

    knight_1.take_damage(damage_to_1)
    knight_2.take_damage(damage_to_2)


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    knights: Dict[str, Knight] = {}

    # Criar todos os knights dinamicamente
    for key, config in knights_config.items():
        knights[key] = Knight(config)

    # Executar as batalhas (mantendo a mesma lógica original)
    fight(knights["lancelot"], knights["mordred"])
    fight(knights["arthur"], knights["red_knight"])

    # Construir o resultado dinamicamente
    results: Dict[str, int] = {}

    for knight in knights.values():
        results[knight.name] = knight.hp

    return results
