class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        self.base_power = power
        self.base_hp = hp

    def prepare_for_battle(self) -> None:

        self.power = self.base_power
        self.hp = self.base_hp
        self.protection = 0

        if self.armour:
            for armour in self.armour:
                self.protection += armour["protection"]

        if self.potion:
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

        self.power += self.weapon["power"]
