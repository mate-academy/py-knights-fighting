def calculate_total_protection(armour: list) -> int:
    total_protection = 0
    for item in armour:
        total_protection += item["protection"]
    return total_protection


def enhance_knight_power(knight: dict, weapon_power: int) -> None:
    knight["power"] += weapon_power


def apply_potion_effects(knight: dict,
                         potion: dict) -> None:
    if potion is not None:
        attributes = ["power", "protection", "hp"]
        for attribute in attributes:
            if attribute in potion["effect"]:
                knight[attribute] += potion["effect"][attribute]


def battle_preparation(knight: dict) -> dict:
    knight["protection"] = calculate_total_protection(knight["armour"])
    enhance_knight_power(knight, knight["weapon"]["power"])
    apply_potion_effects(knight, knight["potion"])
    return knight
