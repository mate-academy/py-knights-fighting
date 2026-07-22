from typing import TypedDict


class EffectiveStats(TypedDict):
    name: str
    power: int
    hp: int
    protection: int


def calculate_protection(armour: list) -> int:
    return sum(piece["protection"] for piece in armour)


def apply_potion(stats: EffectiveStats, potion: dict | None) -> None:
    if potion is None:
        return

    effect = potion["effect"]
    stats["power"] += effect.get("power", 0)
    stats["protection"] += effect.get("protection", 0)
    stats["hp"] += effect.get("hp", 0)


def calculate_effective_stats(config: dict) -> EffectiveStats:
    stats: EffectiveStats = {
        "name": config["name"],
        "power": config["power"] + config["weapon"]["power"],
        "hp": config["hp"],
        "protection": calculate_protection(config["armour"]),
    }
    apply_potion(stats, config["potion"])

    return stats
