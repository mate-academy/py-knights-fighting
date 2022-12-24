class KnightPreparation:

    def __init__(self, knight_info: dict) -> None:
        self.knight_info = knight_info
        self.name = knight_info["name"]
        self.hp = knight_info["hp"]
        self.power = knight_info["power"]
        self.armour = knight_info["armour"]
        self.weapon = knight_info["weapon"]
        self.potion = knight_info["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        for ar in self.armour:
            self.protection += ar["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += \
                    self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += \
                    self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += \
                    self.potion["effect"]["hp"]

    def prepare_knight(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
