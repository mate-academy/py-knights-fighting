from bdb import effective


def potion_power_hp_protection(knights_config: dict) -> dict:
    count = 0
    knight_details = {}

    for name, dict_knife in knights_config.items():
        effect = dict_knife["potion"]["effect"] if (
                dict_knife["potion"] is not None) else {}
        knight_details[name] = {"hp": 0,
                                    "power": 0,
                                    "protection": 0}
        for key in ["hp", "power", "protection"]:
            value = effect.get(key, 0)
            knight_details[name][key] = value
    return knight_details
