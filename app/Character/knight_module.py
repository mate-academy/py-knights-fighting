class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict] = None,
                 weapon: dict = None,
                 potion: dict[dict] = None,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def gear_up(self) -> None:
        self.__class__.protection = 0
        self.power += self.weapon["power"]

        if self.armour:
            self.protection += sum(part["protection"]
                                   for part in self.armour)

        if isinstance(self.potion, dict) and "effect" in self.potion:
            self.hp += self.potion["effect"].get("hp", 0)
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion[
                "effect"].get("protection", 0)
