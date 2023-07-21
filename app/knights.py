class Knight:
    def __init__(self, name: str,
                 power: int,
                 hp: int,
                 armour: list[dict] = None,
                 weapon: dict = None,
                 potion: dict = None,
                 protection: int = 0
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_armour(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        if self.weapon is not None:
            self.power += self.weapon.get("power")

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

    def prepare(self) -> None:
        self.apply_potion()
        self.apply_weapon()
        self.apply_armour()
