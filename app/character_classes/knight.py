class Knight:
    def __init__(
            self,
            name: int,
            power: int,
            hp: int,
            armour: dict,
            weapon: dict,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = sum(item["protection"] for item in self.armour)
        self.power += self.weapon["power"]

        if self.potion is not None:
            self.apply_potion_effects()

    def apply_potion_effects(self) -> None:
        if self.potion is not None:
            for attribute, value in self.potion["effect"].items():
                if attribute in ["power", "protection", "hp"]:
                    setattr(self, attribute, getattr(self, attribute) + value)

    def take_damage(self, damage: int) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
