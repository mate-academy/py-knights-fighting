class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: None | dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.protection = 0
        self.weapon = weapon
        self.potion = potion

    def battle_preparation(self) -> None:
        potion_stats = ["power", "hp", "protection"]

        if self.armour:
            for armour_part in self.armour:
                self.protection += armour_part["protection"]

        self.power += self.weapon["power"]

        if self.potion:
            for stat in potion_stats:
                if stat in self.potion["effect"]:
                    current_value = getattr(self, stat)
                    bonus = self.potion["effect"][stat]
                    setattr(self, stat, current_value + bonus)
