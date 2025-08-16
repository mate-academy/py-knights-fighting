class Knight:
    def __init__(self, name: str, weapon: dict, power: int,
                 hp: int, armour: list, potion: dict = None) -> None:
        self.name = name
        self.weapon = weapon
        self.power_base = power
        self.armour = armour
        self.hp_base = hp
        self.potion = potion

        self.hp = hp
        self.power = power
        self.protection = 0

    def battle_preparation(self) -> None:
        self.apply_armour()
        self.apply_potion()
        self.apply_weapon()

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"] :
                self.protection += self.potion["effect"]["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]
