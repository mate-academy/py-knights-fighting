class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: (None, dict),
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_armour(self) -> None:
        for arms in self.armour:
            self.protection += arms["protection"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for name_attribute, effect_potion in self.potion["effect"].items():
                attribute = getattr(self, name_attribute)
                setattr(self, name_attribute, attribute + effect_potion)
