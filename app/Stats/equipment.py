class Equipment:
    def __init__(self,
                 weapon: dict,
                 armour: list,
                 potion: dict | None
                 ) -> None:

        self.equip_list = [armour_part["part"] for armour_part in armour]
        self.equip_list.append(weapon["name"])
        self.power_boost = weapon["power"]
        self.hp_boost = 0
        self.prot = sum(armour_part["protection"] for armour_part in armour)

        if potion:
            potion_name = potion["name"]
            self.equip_list.append(f"Potion of {potion_name}")
            effects = potion["effect"]
            if "power" in effects:
                self.power_boost += effects["power"]
            if "hp" in effects:
                self.hp_boost += effects["hp"]
            if "protection" in effects:
                self.prot += effects["protection"]
