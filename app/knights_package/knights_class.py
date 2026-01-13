class Knights:

    def __init__(
            self, name: str, power: int, hp: int,
            armour: list, weapon: dict, potion: dict | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def battle_preparation(self) -> None:

        # apply armour
        self.protection = sum([arm["protection"] for arm in self.armour])

        # apply weapon
        self.power += self.weapon["power"]

        # apply potion if exist
        if self.potion is not None and self.potion.get("effect") is not None:
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)
            self.hp += self.potion["effect"].get("hp", 0)

    def hp_calculation(self, other: "Knights") -> None:
        if isinstance(other, Knights):
            self.hp -= other.power - self.protection
            if self.hp <= 0:
                self.hp = 0
