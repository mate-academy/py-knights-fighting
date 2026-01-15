class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict | None],
            weapon: dict,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        if self.armour:
            for armour in self.armour:
                self.protection += armour["protection"]

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

    def get_hp(self) -> str:
        return f"{self.name} has {self.hp} hp"
