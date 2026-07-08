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

        if self.potion:
            self.hp += self.potion["effect"].get("hp", 0)

    def protections(self) -> int:
        protection = sum(item["protection"] for item in self.armour)

        if self.potion:
            protection += self.potion["effect"].get("protection", 0)

        return protection

    def powers(self) -> int:
        power = self.power + self.weapon["power"]

        if self.potion:
            power += self.potion["effect"].get("power", 0)

        return power
