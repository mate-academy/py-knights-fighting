from typing import Dict
from app.battle_config import start_battles
from app.knights import Knight
from app.knights_data import KNIGHTS


def battle_knights(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config: Dict = KNIGHTS) -> Dict:
    results = start_battles(knights_config, battle_knights)
    return results
