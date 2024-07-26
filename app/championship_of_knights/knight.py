class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def applying_armor(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def applying_weapon(self) -> None:
        self.power += self.weapon["power"]

    def applying_potion(self) -> None:
        if self.potion is not None:
            for attr, value in self.potion["effect"].items():
                setattr(self, attr, getattr(self, attr) + value)

    def battle_preparations(self) -> None:
        self.applying_armor()
        self.applying_weapon()
        self.applying_potion()
