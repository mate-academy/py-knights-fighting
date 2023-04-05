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
            if self.potion["effect"].get("power"):
                self.power += self.potion["effect"]["power"]
            if self.potion["effect"].get("protection"):
                self.protection += self.potion["effect"]["protection"]
            if self.potion["effect"].get("hp"):
                self.hp += self.potion["effect"]["hp"]
