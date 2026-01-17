class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: dict,
            weapon: dict,
            potion: dict,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def use_weapon(self) -> None:
        self.power += self.weapon["power"]

    def use_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def use_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]

            attributes = ["hp", "power", "protection"]

            for attribute in attributes:
                if attribute in effect:
                    current_value = getattr(self, attribute)
                    setattr(self, attribute, current_value + effect[attribute])

    def apply_factors(self) -> None:
        self.use_potion()
        self.use_armour()
        self.use_weapon()
