class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict = None) -> None:
        self.name = name
        self.power_base = power
        self.hp_base = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.power = power
        self.hp = hp
        self.protection = 0

    def battle_preparations(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

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
