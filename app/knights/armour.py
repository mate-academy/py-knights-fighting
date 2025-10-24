def armour_protection(knights_config: dict) -> dict:
    armour_prot = {}
    for name, dict_knife in knights_config.items():
        armour_power_for_knights = 0
        if len(dict_knife["armour"]) >= 1:
            for armour_dict in dict_knife["armour"]:
                if "protection" in armour_dict:
                    armour_power_for_knights += armour_dict["protection"]
        armour_prot[name] = armour_power_for_knights
    return armour_prot
