class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict],
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

    def add_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def add_weapon(self) -> None:
        self.power += self.weapon["power"]

    def add_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion["effect"]
            for attribute, value in effect.items():
                current_value = getattr(self, attribute)
                setattr(self, attribute, current_value + value)

    def decrease_hp(self, damage: int) -> None:
        self.hp -= max(0, damage)
        if self.hp < 0:
            self.hp = 0
