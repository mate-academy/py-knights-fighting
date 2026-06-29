class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.armour = knight_data["armour"]
        self.weapon = knight_data["weapon"]
        self.potion = knight_data["potion"]
        self.protection = 0

    def apply_equipment(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]

            if "protection" in effect:
                self.protection += effect["protection"]

            if "hp" in effect:
                self.hp += effect["hp"]
