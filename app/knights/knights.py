def knights(knights_config: dict) -> dict:
    knights_power_hp = {}
    for name, dict_knife in knights_config.items():
        knights_power_hp[name] = {"hp": dict_knife["hp"],
                                  "power": dict_knife["power"],
                                  "knight_name": dict_knife["name"]}
    return knights_power_hp
