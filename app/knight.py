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

    def prepare_for_battle(self) -> None:
        self.power += self.weapon["power"]
        for piece in self.armour:
            self.protection += piece["protection"]
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
