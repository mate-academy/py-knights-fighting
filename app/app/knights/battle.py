from typing import Dict

from .knight import Knight


def prepare_knights(knights_config: Dict[str, Dict]) -> Dict[str, Knight]:
    """Tworzy rycerzy na podstawie configu i przygotowuje ich do walki."""
    knights = {
        key: Knight.from_config(config)
        for key, config in knights_config.items()
    }

    for knight in knights.values():
        knight.prepare_for_battle()

    return knights


def duel(first: Knight, second: Knight) -> None:
    """Pojedynek dwóch rycerzy – dokładnie ta sama formuła co w oryginale."""
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection

    if first.hp <= 0:
        first.hp = 0

    if second.hp <= 0:
        second.hp = 0
