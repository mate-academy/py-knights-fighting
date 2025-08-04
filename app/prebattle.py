def preparations(knigtsconfig: dict) -> dict:
    for name, knight in knigtsconfig.items():
        knight["protection"] = 0
        for one in knight["armour"]:
            knight["protection"] += one["protection"]

        knight["power"] += knight["weapon"]["power"]

        if knight["potion"] is not None:
            if "power" in knight["potion"]["effect"]:
                knight["power"] += knight["potion"]["effect"]["power"]

            if "protection" in knight["potion"]["effect"]:
                knight["protection"] +=\
                    (knight)["potion"]["effect"]["protection"]

            if "hp" in knight["potion"]["effect"]:
                knight["hp"] += knight["potion"]["effect"]["hp"]

    return knigtsconfig
