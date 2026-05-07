def apply_armour(knight: dict, statistic: dict) -> None:
    protection = 0
    for armour in knight["armour"]:
        protection += armour.get("protection", 0)
    statistic["protection"] = protection


def apply_weapon(knight: dict, statistic: dict) -> None:
    statistic["power"] += knight["weapon"]["power"]


def apply_potion(knight: dict, statistic: dict) -> None:
    if knight["potion"] is not None:
        effects = knight["potion"]["effect"]
        for effect, effect_val in effects.items():
            statistic[effect] += effect_val


def battle_preparation(knight: dict) -> dict:
    knight_stats = {
        "name": knight.get("name", "Noname"),
        "hp": knight.get("hp", 0),
        "power": knight.get("power", 0),
        "protection": 0,
    }
    apply_armour(knight, knight_stats)
    apply_weapon(knight, knight_stats)
    apply_potion(knight, knight_stats)
    return knight_stats
