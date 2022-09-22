class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict,
                 potion: (dict, None) = None) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:

        for a in self.armour:
            self.protection += a["protection"]

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

    def get_ready(self) -> None:
        self.apply_armour()
        self.apply_potion()
        self.apply_weapon()
