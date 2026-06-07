from typing import Iterator
from app.knights.knights import Knight


def create_knight(knights_stats: dict) -> Iterator[Knight]:
    for one_knight, stats in knights_stats.items():
        knight_obj = Knight(
            name=stats["name"],
            hp=stats["hp"],
            power=stats["power"]
        )
        knight_obj.apply_armour(stats["armour"])
        knight_obj.apply_weapon(stats["weapon"])
        knight_obj.apply_potion(stats["potion"])
        yield knight_obj


def battle(knights_stats: dict) -> dict:
    ready_knights = {
        knight.name: knight for knight in create_knight(knights_stats)
    }

    ready_knights["Lancelot"].take_damage(ready_knights["Mordred"].power)
    ready_knights["Mordred"].take_damage(ready_knights["Lancelot"].power)

    ready_knights["Arthur"].take_damage(ready_knights["Red Knight"].power)
    ready_knights["Red Knight"].take_damage(ready_knights["Arthur"].power)

    return {
        "Lancelot": ready_knights["Lancelot"].hp,
        "Arthur": ready_knights["Arthur"].hp,
        "Mordred": ready_knights["Mordred"].hp,
        "Red Knight": ready_knights["Red Knight"].hp
    }
