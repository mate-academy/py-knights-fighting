from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, Iterable, Tuple


def _total_protection(armour: Iterable[Dict[str, Any]]) -> int:
    return sum(int(piece["protection"]) for piece in (armour or []))


def _apply_potion(
    hp: int,
    power: int,
    protection: int,
    potion: Dict[str, Any] | None,
) -> Tuple[int, int, int]:
    if not potion:
        return hp, power, protection
    effect = potion.get("effect", {}) or {}
    return (
        hp + int(effect.get("hp", 0)),
        power + int(effect.get("power", 0)),
        protection + int(effect.get("protection", 0)),
    )


def _prepare_knight(raw: Dict[str, Any]) -> Dict[str, Any]:
    hp = int(raw["hp"])
    base_power = int(raw["power"])
    weapon_power = int(raw["weapon"]["power"])
    protection = _total_protection(raw.get("armour", []))

    power = base_power + weapon_power
    hp, power, protection = _apply_potion(
        hp,
        power,
        protection,
        raw.get("potion"),
    )

    return {
        "name": str(raw["name"]),
        "hp": hp,
        "power": power,
        "protection": protection,
    }


def _duel_once(
    knight_a: Dict[str, Any],
    knight_b: Dict[str, Any],
) -> None:
    knight_a["hp"] -= knight_b["power"] - knight_a["protection"]
    knight_b["hp"] -= knight_a["power"] - knight_b["protection"]

    if knight_a["hp"] <= 0:
        knight_a["hp"] = 0
    if knight_b["hp"] <= 0:
        knight_b["hp"] = 0


def battle(knights_config: Dict[str, Any]) -> Dict[str, int]:
    cfg = deepcopy(knights_config)

    lancelot = _prepare_knight(cfg["lancelot"])
    arthur = _prepare_knight(cfg["arthur"])
    mordred = _prepare_knight(cfg["mordred"])
    red_knight = _prepare_knight(cfg["red_knight"])

    _duel_once(lancelot, mordred)
    _duel_once(arthur, red_knight)

    return {
        lancelot["name"]: lancelot["hp"],
        arthur["name"]: arthur["hp"],
        mordred["name"]: mordred["hp"],
        red_knight["name"]: red_knight["hp"],
    }
