class Preparing:
    def __init__(self, knight_config: dict) -> None:
        self.name = knight_config["name"]
        self.power = knight_config["power"]
        self.hp = knight_config["hp"]
        self.armour = knight_config["armour"]
        self.weapon = knight_config["weapon"]
        self.potion = knight_config["potion"]
        self.protection = 0
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion_if_exist()

    def apply_armour(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
