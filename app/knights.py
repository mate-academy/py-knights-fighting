class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.weapon = knight["weapon"]
        self.power = knight["power"]
        self._calculate_power()
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.potion = knight["potion"]
        self.protection = 0
        self._calculate_protection()
        self._calculate_potion()

    def _calculate_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def _calculate_power(self) -> None:
        self.power += self.weapon["power"]

    def _calculate_protection(self) -> None:
        self.protection = sum(armour["protection"] for armour in self.armour)
