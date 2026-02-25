class Knight:
    def __init__(self, name: str,
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
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
            self.protection += effect.get("protection", 0)
