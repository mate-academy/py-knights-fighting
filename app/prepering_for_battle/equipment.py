class ApplyEquipment:

    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def prepare_for_battle(self) -> None:
        # apply armour
        self.knight["protection"] = 0
        for armour_element in self.knight["armour"]:
            self.knight["protection"] += armour_element["protection"]

        # apply weapon
        self.knight["power"] += self.knight["weapon"]["power"]

        # apply potion if exist
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.knight["power"] += (
                    self.knight["potion"]["effect"]["power"]
                )
            if "protection" in self.knight["potion"]["effect"]:
                self.knight["protection"] += (
                    self.knight["potion"]["effect"]["protection"]
                )
            if "hp" in self.knight["potion"]["effect"]:
                self.knight["hp"] += self.knight["potion"]["effect"]["hp"]
