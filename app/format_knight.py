def format(knightsConfig):
    knight_states = {}

    for knight in knightsConfig.values():

        knight["protection"] = 0
        for add_protection in knight["armour"]:
            knight["protection"] += add_protection["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"]:
            for effect_name, effect_value in knight["potion"]["effect"].items():
                if effect_name == "power":
                    knight["power"] += effect_value

                if effect_name == "protection":
                    knight["protection"] += effect_value

                if  effect_name == "hp":
                    knight["hp"] += effect_value

        knight_states[knight["name"]] = {"hp": knight["hp"], "power": knight["power"], "protection": knight["protection"]}
    return knight_states