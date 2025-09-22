from __future__ import annotations

from typing import Dict

from .models import Armour, Knight, Potion, Stats, Weapon


def _build_armour_list(cfg_list) -> list[Armour]:
    if not cfg_list:
        return []
    result: list[Armour] = []
    for item in cfg_list:
        result.append(
            Armour(
                part=str(item.get("part", "")),
                protection=int(item.get("protection", 0)),
            )
        )
    return result


def _build_weapon(cfg: dict) -> Weapon:
    if not cfg or "power" not in cfg:
        raise ValueError(
            "Each knight must have a weapon with 'power'."
        )
    return Weapon(
        name=str(cfg.get("name", "")),
        power=int(cfg["power"]),
    )


def _build_potion(cfg: dict | None) -> Potion | None:
    if not cfg:
        return None
    effect = cfg.get("effect", {}) or {}
    filtered = {
        k: int(v)
        for k, v in effect.items()
        if k in {"hp", "power", "protection"}
    }
    return Potion(
        name=str(cfg.get("name", "")), effect=filtered
    )


def build_knight(data: dict) -> Knight:
    if not data:
        raise ValueError("Knight config is empty.")

    name = str(data.get("name", "")).strip()
    if not name:
        raise ValueError("Knight must have a 'name'.")

    base_power = int(data.get("power", 0))
    base_hp = int(data.get("hp", 0))
    armour = _build_armour_list(data.get("armour", []))
    weapon = _build_weapon(data.get("weapon"))
    potion = _build_potion(data.get("potion"))

    return Knight(
        name=name,
        base_power=base_power,
        base_hp=base_hp,
        armour=armour,
        weapon=weapon,
        potion=potion,
    )


def build_all(
    knights_cfg: Dict[str, dict],
) -> Dict[str, Knight]:
    return {
        key: build_knight(value)
        for key, value in knights_cfg.items()
    }


def empty_stats_for(knight: Knight) -> Stats:
    return Stats(
        name=knight.name,
        hp=knight.base_hp,
        power=knight.base_power,
        protection=0,
    )
