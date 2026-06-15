def potion(knights_dict: dict) -> None:
    for key, knight in knights_dict.items():
        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] \
                    += knight["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]
