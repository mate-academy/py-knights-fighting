class Knight:

    def __init__(
            self,
            name: str,
            hp: int,
            power: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = 0
        for item in self.armour:
            self.protection += item["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def battle_with(self, another: Knight) -> None:

        self.hp -= another.power - self.protection
        another.hp -= self.power - another.protection

        if self.hp <= 0:
            self.hp = 0

        if another.hp <= 0:
            another.hp = 0
