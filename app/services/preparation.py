from __future__ import annotations

from app.domain.types import ArmourPart, KnightConfig, KnightStats, Potion


def _armour_protection(armour: list[ArmourPart]) -> int:
    return sum(armour_part["protection"] for armour_part in armour)


def _apply_potion(stats: KnightStats, potion: Potion | None) -> None:
    if potion is None:
        return

    effect = potion.get("effect", {})
    if "hp" in effect:
        stats["hp"] += int(effect["hp"])
    if "power" in effect:
        stats["power"] += int(effect["power"])
    if "protection" in effect:
        stats["protection"] += int(effect["protection"])


def prepare_knight(knight: KnightConfig) -> KnightStats:
    """
    Creates battle-ready stats for a knight according to the task rules:
    - protection = sum of armour protections (base is 0)
    - power += weapon.power
    - apply potion effects if potion exists
    """
    stats: KnightStats = {
        "name": knight["name"],
        "hp": int(knight["hp"]),
        "power": int(knight["power"]) + int(knight["weapon"]["power"]),
        "protection": _armour_protection(knight.get("armour", [])),
    }

    _apply_potion(stats, knight.get("potion"))
    return stats
