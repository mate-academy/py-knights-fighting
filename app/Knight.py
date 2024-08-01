class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            weapon: dict,
            armour: list = [],
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour
        self.potion = potion
        self.protection = 0

        self.protection_count()
        self.power_count()
        self.potion_count()

    def protection_count(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def power_count(self) -> None:
        self.power += self.weapon["power"]

    def potion_count(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
