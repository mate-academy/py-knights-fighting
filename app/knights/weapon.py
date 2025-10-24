def weapon_power_count(knights_config: dict) -> dict:
    weapon_power = {}
    for name, knight_details in knights_config.items():
        power = 0
        if "weapon" in knight_details:
            if "power" in knight_details["weapon"]:
                power += knight_details["weapon"]["power"]

        weapon_power[name] = power
    return weapon_power
