class Knight:
    def __init__(self, knights_config: dict) -> None:
        self.name = knights_config["name"]
        self.hp = knights_config["hp"]

        self.armour = knights_config["armour"]
        self.protection = self.apply_armour()

        self.weapon = knights_config["weapon"]
        self.power = knights_config["power"] + self.weapon["power"]

        self.potion = knights_config["potion"]
        self.potion_aply()

    def potion_aply(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def apply_armour(self) -> int:
        if not self.armour:
            return 0
        protection = 0
        for armour_part in self.armour:
            protection += armour_part["protection"]
        return protection

    def check_hp(self) -> int | None:
        if self.hp < 0:
            self.hp = 0
