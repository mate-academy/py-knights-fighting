def knights(knights_config: dict) -> dict:
    knights_power_hp = {}
    for name, knife_data in knights_config.items():
        knights_power_hp[name] = {"hp": knife_data["hp"],
                                  "power": knife_data["power"],
                                  "knight_name": knife_data["name"]}
    return knights_power_hp
