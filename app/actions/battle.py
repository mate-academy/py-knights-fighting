from app.actions.register import register_knights
from app.people.knight import Knight


def _duel(knight1: Knight, knight2: Knight) -> None:
    knight1.hp -= max(0, knight2.power - knight1.protection)
    knight2.hp -= max(0, knight1.power - knight2.protection)


def battle(registered_knights: list) -> dict:
    if isinstance(registered_knights, dict):
        registered_knights = register_knights(registered_knights)

    for knight in registered_knights:
        knight.prepare_for_battle()

    _duel(registered_knights[0], registered_knights[2])
    _duel(registered_knights[1], registered_knights[3])

    for knight in registered_knights:
        if knight.hp <= 0:
            knight.hp = 0

    results = {}

    for knight in registered_knights:
        results[knight.name] = knight.hp

    return results
