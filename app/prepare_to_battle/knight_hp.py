def hp(knight: dict) -> int:
    total_hp = knight["hp"]
    hp_potion = knight["potion"]
    if hp_potion:
        if hp_potion["effect"].get("hp"):
            total_hp += hp_potion["effect"]["hp"]
    return total_hp
