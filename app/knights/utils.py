def apply_armor(knight: dict) -> float:
    protection = 0
    for armour in knight["armour"]:
        protection += armour["protection"]
    return protection


def apply_weapon(knight: dict) -> float:
    return knight["weapon"]["power"]


def apply_potion(knight: dict) -> tuple:
    power = 0
    protection = 0
    hp = 0

    if knight["potion"]:
        if "power" in knight["potion"]["effect"]:
            power = knight["potion"]["effect"]["power"]
        if "protection" in knight["potion"]["effect"]:
            protection = knight["potion"]["effect"]["protection"]
        if "hp" in knight["potion"]["effect"]:
            hp = knight["potion"]["effect"]["hp"]

    return power, protection, hp


def calculate_knight_stats(knight: dict) -> tuple:
    protection = apply_armor(knight)
    weapon_power = apply_weapon(knight)
    potion_power, potion_protection, potion_hp = apply_potion(knight)

    total_power = knight["power"] + weapon_power + potion_power
    total_protection = protection + potion_protection
    total_hp = knight["hp"] + potion_hp

    return total_power, total_hp, total_protection
