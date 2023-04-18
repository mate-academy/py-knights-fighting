from __future__ import annotations
from typing import Any

from app.knights.knight import Knight
from app.actions.fight import knight_fight


def create_knight(knight_config: dict[str, Any]) -> dict[str, Knight]:
    return {knight_name: Knight(knight_stats["name"],
                                knight_stats["power"],
                                knight_stats["hp"],
                                knight_stats["armour"],
                                knight_stats["weapon"],
                                knight_stats["potion"])
            for knight_name, knight_stats in knight_config.items()}


def battle(knight_config: dict[str, Any]) -> dict[str, int]:
    ready_knights = create_knight(knight_config)
    print(ready_knights["lancelot"].hp)
    print(ready_knights["lancelot"].power)
    print(ready_knights["lancelot"].protection)
    knight_fight(ready_knights["lancelot"], ready_knights["mordred"])
    print(ready_knights["lancelot"].hp)
    print(ready_knights["lancelot"].power)
    print(ready_knights["lancelot"].protection)
    knight_fight(ready_knights["arthur"], ready_knights["red_knight"])
    return {
        "Lancelot": ready_knights["lancelot"].hp,
        "Artur": ready_knights["arthur"].hp,
        "Mordred": ready_knights["mordred"].hp,
        "Red Knight": ready_knights["red_knight"].hp
    }
