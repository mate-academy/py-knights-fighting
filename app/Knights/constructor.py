class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        # apply armour, weapon, potion if exist
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion_if_exist()

    def apply_armor(self) -> list:
        for armour in self.armour:
            self.protection += armour["protection"]
        return self.armour

    def apply_weapon(self) -> int:
        self.power = self.power + self.weapon["power"]
        return self.power

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            for key in effect:
                setattr(self, key, getattr(self, key, 0) + effect[key])
