class Knights:

    def __init__(self, knight: dict) -> None:
        self.knight = knight
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.power = knight["power"]
        self.protection = 0
        self.add_armour()
        self.add_weapon()
        self.add_from_potion()

    def add_armour(self) -> None:
        for a in self.knight["armour"]:
            self.protection += a["protection"]

    def add_weapon(self) -> None:
        self.power += self.knight["weapon"]["power"]

    def add_from_potion(self) -> None:
        if self.knight["potion"] is not None:
            if "power" in self.knight["potion"]["effect"]:
                self.power += self.knight["potion"]["effect"]["power"]

            if "protection" in self.knight["potion"]["effect"]:
                self.protection += \
                    self.knight["potion"]["effect"]["protection"]

            if "hp" in self.knight["potion"]["effect"]:
                self.hp += self.knight["potion"]["effect"]["hp"]
