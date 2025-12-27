def knight_weapon(knight: dict) -> int:
    total_power = knight["power"]
    total_power += knight["weapon"]["power"]
    power_potion = knight["potion"]
    if power_potion:
        if power_potion["effect"].get("power"):
            total_power += power_potion["effect"]["power"]
    return total_power
