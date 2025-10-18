class Fighter:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armours: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armours = armours
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for armor in self.armours:
            self.protection += armor["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion and "effect" in self.potion:
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)
            self.hp += self.potion["effect"].get("hp", 0)
