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
        self.hp = hp
        self.power = power
        self.weapon = weapon
        self.armor = armour
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        protection = 0
        for part in self.armor:
            protection += part["protection"]
        self.protection = protection

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            for attribute, value in self.potion["effect"].items():
                self.__setattr__(
                    attribute,
                    self.__getattribute__(attribute) + value
                )

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
