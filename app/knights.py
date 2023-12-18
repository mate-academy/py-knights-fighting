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

    def get_power(self) -> None:
        self.power += self.weapon["power"]

    def get_protection(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def use_potion(self) -> None:
        if self.potion is not None:
            if isinstance(self.potion["effect"], dict):
                for key, value in self.potion["effect"].items():
                    setattr(self, key,
                            getattr(self, key) + value)

    def use_basic_stats(self) -> None:
        self.use_potion()
        self.get_protection()
        self.get_power()
