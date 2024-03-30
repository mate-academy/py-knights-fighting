from app.battle_config import start_battles
from app.knights_data import KNIGHTS


def battle_knights(knight1, knight2):
    knight1.hp -= knight2.power - knight1.protection
    knight2.hp -= knight1.power - knight2.protection

    if knight1.hp <= 0:
        knight1.hp = 0

    if knight2.hp <= 0:
        knight2.hp = 0


def battle(knights_config=KNIGHTS):
    results = start_battles(knights_config, battle_knights)
    return results
