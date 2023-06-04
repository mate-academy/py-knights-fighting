from __future__ import annotations

from app.knights.knights import Knight, KnightBeforeBattle


def create_knights_list(knights: dict) -> list[Knight]:
    return [
        Knight(
            name=knight,
            power=info["power"],
            hp=info["hp"],
            weapon=info["weapon"],
            armour=info["armour"] if info.get("armour") else None,
            potion=info["potion"] if info.get("potion") else None
        )
        for knight, info in knights.items()
    ]


def invite_knights_for_battle(
        knights: list[Knight]
) -> list[KnightBeforeBattle]:
    return [
        KnightBeforeBattle(
            name=knight.name,
            hp=knight.total_hp(),
            power=knight.total_power(),
            protection=knight.total_protection()
        )
        for knight in knights
    ]
