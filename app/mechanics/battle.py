from __future__ import annotations

from typing import Any, Dict, Optional

from app.domain.models import Armour, Knight, Potion, Weapon


def _as_armour(items: Optional[list[dict]]) -> list[Armour]:
    if not items:
        return []
    return [
        Armour(
            part=str(item["part"]),
            protection=int(item["protection"]),
        )
        for item in items
    ]


def _as_weapon(item: dict) -> Weapon:
    return Weapon(name=str(item["name"]), power=int(item["power"]))


def _as_potion(item: Optional[dict]) -> Optional[Potion]:
    if item is None:
        return None
    effect = item.get("effect", {}) or {}
    return Potion(
        name=str(item["name"]),
        hp=int(effect.get("hp", 0)),
        power=int(effect.get("power", 0)),
        protection=int(effect.get("protection", 0)),
    )


def build_knight(config: Dict[str, Any]) -> Knight:
    knight = Knight(
        name=str(config["name"]),
        base_power=int(config["power"]),
        base_hp=int(config["hp"]),
        armour=_as_armour(config.get("armour")),
        weapon=_as_weapon(config["weapon"]),
        potion=_as_potion(config.get("potion")),
    )
    knight.prepare_for_battle()
    return knight


def duel_one_round(
    knight_first: Knight,
    knight_second: Knight,
) -> None:
    knight_first.hp -= (
        knight_second.power - knight_first.protection
    )
    knight_second.hp -= (
        knight_first.power - knight_second.protection
    )

    if knight_first.hp <= 0:
        knight_first.hp = 0
    if knight_second.hp <= 0:
        knight_second.hp = 0
