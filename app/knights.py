class Knights:

    def __init__(self, name: str,
                 hp: int,
                 armour: list,
                 power: int,
                 weapon: int,
                 potion: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]
            if "protection" in effect:
                self.protection += effect["protection"]
            if "hp" in effect:
                self.hp += effect["hp"]

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
