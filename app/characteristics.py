def characteristic(knightsconfig: dict) -> dict:
    for _, characteristics in knightsconfig.items():
        characteristics["protection"] = 0
        for bonus in characteristics["armour"]:
            characteristics["protection"] += bonus["protection"]

        characteristics["power"] += characteristics["weapon"]["power"]

        if characteristics["potion"] is not None:
            if "power" in characteristics["potion"]["effect"]:
                characteristics["power"] += (
                    characteristics)["potion"]["effect"]["power"]

            if "protection" in characteristics["potion"]["effect"]:
                characteristics["protection"] += (
                    characteristics)["potion"]["effect"]["protection"]

            if "hp" in characteristics["potion"]["effect"]:
                characteristics["hp"] += (
                    characteristics)["potion"]["effect"]["hp"]
    return knightsconfig
