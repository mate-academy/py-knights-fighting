def apply_potion(stats: dict, potion: dict | None) -> dict:
    if not potion:
        return stats

    effect = potion["effect"]

    stats["hp"] += effect.get("hp", 0)
    stats["power"] += effect.get("power", 0)
    stats["protection"] += effect.get("protection", 0)

    return stats
