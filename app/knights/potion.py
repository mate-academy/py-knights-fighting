from bdb import effective


def potion_power_hp_protection(knights_config: dict) -> dict:
    count = 0
    potion_for_knights = {}

    for name, dict_knife in knights_config.items():
        potion_hp = 0
        potion_power = 0
        potion_protection = 0

        effect = dict_knife["potion"]["effect"] if (
                dict_knife["potion"] is not None) else {}
        potion_for_knights[name] = {"hp": 0,
                                    "power": 0,
                                    "protection": 0}
        for key in ["hp", "power", "protection"]:
            value = effect.get(key, 0)
            potion_for_knights[name][key] = value
        count += 1
    return potion_for_knights

# def potion_power_hp_protection(knights_config: dict) -> dict:
#     count = 0
#     potion_for_knights = {}
#
#     for name, dict_knife in knights_config.items():
#         potion_hp = 0
#         potion_power = 0
#         potion_protection = 0
#
#         if dict_knife["potion"] is not None:
#             if "hp" in dict_knife["potion"]["effect"]:
#                 potion_hp += (
#                     dict_knife)["potion"]["effect"]["hp"]
#             if "power" in dict_knife["potion"]["effect"]:
#                 potion_power += (
#                     dict_knife)["potion"]["effect"]["power"]
#             if "protection" in dict_knife["potion"]["effect"]:
#                 potion_protection += (
#                     dict_knife)["potion"]["effect"]["protection"]
#
#         potion_for_knights[name] = {"hp": potion_hp,
#                                     "power": potion_power,
#                                     "protection": potion_protection}
#         count += 1
#     return potion_for_knights
