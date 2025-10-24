def weapon_power_count(knights_config: dict) -> dict:
    count = 0
    weapon_power = {}
    for name, dict_knife in knights_config.items():
        power = 0
        if "weapon" in dict_knife:
            if "power" in dict_knife["weapon"]:
                power += dict_knife["weapon"]["power"]
        count += 1
        weapon_power[name] = power
    return weapon_power
