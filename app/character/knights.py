class Knights:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effect = self.potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)
