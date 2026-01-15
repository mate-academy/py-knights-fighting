class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict[dict]
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.apply_power()
        self.apply_armour()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = 0
        for ar in self.armour:
            self.protection += ar["protection"]

    def apply_power(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:

        if self.potion:
            for effect_type, effect_value in self.potion.get("effect").items():
                setattr(self, effect_type,
                        getattr(self, effect_type, 0) + effect_value)
