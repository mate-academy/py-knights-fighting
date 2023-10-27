def create_knights_dicts(knights: dict):
    completed_knights = {}

    for knight_name, knight_value in knights.items():
        knights_dicts = {}

        knights_dicts["hp"] = knight_value["hp"]

        knights_dicts["power"] = knight_value["power"]
        if knight_value["weapon"]["power"]:
            knights_dicts["power"] += knight_value["weapon"]["power"]

        if knight_value["armour"]:
            for item in knight_value["armour"]:
                if knights_dicts.get("protection", 0) != 0:
                    knights_dicts["protection"] += item["protection"]
                else:
                    knights_dicts["protection"] = item["protection"]
        else:
            knights_dicts["protection"] = 0

        if knight_value["potion"] is not None:

            if "protection" in knight_value["potion"]["effect"]:
                if knight_value["armour"]:
                    knights_dicts["protection"] += knight_value["potion"]["effect"]["protection"]
                else:
                    knights_dicts["protection"] = knight_value["potion"]["effect"]["protection"]

            if "hp" in knight_value["potion"]["effect"]:
                knights_dicts["hp"] += knight_value["potion"]["effect"]["hp"]

            if "power" in knight_value["potion"]["effect"]:
                knights_dicts["power"] += knight_value["potion"]["effect"]["power"]

        completed_knights[knight_name] = knights_dicts

    return completed_knights
