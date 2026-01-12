# This file contains the core logic for preparing knights and conducting duels.
# These functions are used by the main battle orchestrator.

def _prepare_knight_stats(knight_data: dict) -> dict:
    """Calculates final stats for a single knight based on their equipment."""
    protection = sum(
        part.get("protection", 0) for part in knight_data.get("armour", [])
    )
    power = knight_data["power"] + knight_data["weapon"]["power"]
    hp = knight_data["hp"]

    if knight_data.get("potion"):
        effect = knight_data["potion"].get("effect", {})
        hp += effect.get("hp", 0)
        power += effect.get("power", 0)
        protection += effect.get("protection", 0)

    return {"hp": hp, "power": power, "protection": protection}


def _duel(knight1_stats: dict, knight2_stats: dict) -> tuple[int, int]:
    """Calculates the result of a single duel, returning final HP for both."""
    damage_to_knight1 = max(
        0, knight2_stats["power"] - knight1_stats["protection"]
    )
    hp1_after_battle = knight1_stats["hp"] - damage_to_knight1

    damage_to_knight2 = max(
        0, knight1_stats["power"] - knight2_stats["protection"]
    )
    hp2_after_battle = knight2_stats["hp"] - damage_to_knight2

    return max(0, hp1_after_battle), max(0, hp2_after_battle)
