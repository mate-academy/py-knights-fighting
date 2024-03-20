from __future__ import annotations

from tests.default_config import fights_config

from knights import Knight

def battle(knights_config: dict) -> dict:
    knights = {}

    for name, properties in knights_config.items():
        knight = Knight(**properties)
        knights.update({name: knight})
        knight.activate_items()

    # Lancelot vs Mordred:
    knights["lancelot"].hp -= knights["mordred"].power - knights["lancelot"].protection
    knights["mordred"].hp -= knights["lancelot"].power - knights["mordred"].protection

    # Проверяем, упал ли кто-то в битве
    for knight in ["lancelot", "mordred"]:
        if knights[knight].hp <= 0:
            knights[knight].hp = 0

    # Arthur vs Red Knight:
    knights["arthur"].hp -= knights["red_knight"].power - knights["arthur"].protection
    knights["red_knight"].hp -= knights["arthur"].power - knights["red_knight"].protection

    # Проверяем, упал ли кто-то в битве
    for knight in ["arthur", "red_knight"]:
        if knights[knight].hp <= 0:
            knights[knight].hp = 0
    return {knight.name: knight.hp for knight in knights.values()}


if __name__ == '__main__':
    print(battle(fights_config))
