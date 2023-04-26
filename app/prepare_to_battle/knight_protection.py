def armor_protection(knight: dict) -> int:
    total_protection = 0
    for armour in knight["armour"]:
        total_protection += armour["protection"]

    protection_potion = knight["potion"]
    if protection_potion:
        if protection_potion["effect"].get("protection"):
            total_protection += protection_potion["effect"]["protection"]
    return total_protection
