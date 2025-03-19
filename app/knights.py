class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict,
    ) -> None:
        self.name = name
        self.power = power + weapon["power"]
        self.hp = hp
        self.armour = sum(part["protection"] for part in armour)
        self.potion = potion if potion else None

        if self.potion:
            self.drink_potion(self.potion["effect"])

    def drink_potion(self, effect: dict) -> None:
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.armour += effect.get("protection", 0)
