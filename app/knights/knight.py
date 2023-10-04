class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def name(self, new_name: str) -> None:
        self.name = new_name

    def apply_armour(self) -> None:
        self.protection = 0
        for armour_piece in self.armour:
            self.protection += armour_piece["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for attribute, value in self.potion["effect"].items():
                if hasattr(self, attribute):
                    setattr(self, attribute, getattr(self, attribute) + value)
