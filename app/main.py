from __future__ import annotations
from app.knights import Knights


def ready_to_battle(knight_param: dict) -> Knights:
    knight = Knights(
        name=knight_param["name"],
        hp=knight_param["hp"],
        power=knight_param["power"]
    )
    knight.use_weapon(knight_param["weapon"])
    knight.use_armour(knight_param["armour"])
    knight.use_potion(knight_param["potion"])
    return knight


def battle(knight: dict) -> dict:
    all_knight = {}
    for name, stats in knight.items():
        all_knight[name] = ready_to_battle(knight_param=stats)

    all_knight["lancelot"].fight(other=all_knight["mordred"])
    all_knight["arthur"].fight(other=all_knight["red_knight"])

    return {
        all_knight["lancelot"].name: all_knight["lancelot"].hp,
        all_knight["arthur"].name: all_knight["arthur"].hp,
        all_knight["mordred"].name: all_knight["mordred"].hp,
        all_knight["red_knight"].name: all_knight["red_knight"].hp,
    }
