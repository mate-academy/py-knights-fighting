class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list | None,
            weapon: dict | None,
            potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def apply_armour(self) -> None:
        for arm in self.armour:
            self.protection += arm["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            effect = self.potion["effect"]
            if "power" in effect:
                self.power += effect["power"]

            if "protection" in effect:
                self.protection += effect["protection"]

            if "hp" in effect:
                self.hp += effect["hp"]
