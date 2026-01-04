class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def __str__(self) -> str:
        return (f"Name: {self.name}, Power: {self.power}"
                f"HP: {self.hp}, Protection:{self.protection}")

    def calculate_protection(self) -> None:
        for value in self.armour:
            self.protection += value["protection"]

    def calculate_weapon_power(self) -> None:
        self.power += self.weapon["power"]

    def calculate_potion_buff(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def config(self) -> None:
        self.calculate_protection()
        self.calculate_weapon_power()
        self.calculate_potion_buff()
