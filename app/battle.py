from __future__ import annotations
from app.knights import Knight


def battle(knights_config: dict) -> Knight:
    knights = {name: Knight(**params)
               for name, params in knights_config.items()}

    for knight in knights.values():
        knight.prepare_for_battle()

    knights["lancelot"].take_damage(knights["mordred"].power)
    knights["mordred"].take_damage(knights["lancelot"].power)

    knights["arthur"].take_damage(knights["red_knight"].power)
    knights["red_knight"].take_damage(knights["arthur"].power)

    return {knight.name: knight.hp for knight in knights.values()}
