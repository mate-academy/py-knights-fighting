def armour_protection(knights_config: dict) -> dict:
    armour_prot = {}
    for name, knight_data in knights_config.items():
        total_armour_protection = 0
        if len(knight_data["armour"]) >= 1:
            for armour_dict in knight_data["armour"]:
                if "protection" in armour_dict:
                    total_armour_protection += armour_dict["protection"]
        armour_prot[name] = total_armour_protection
    return armour_prot
