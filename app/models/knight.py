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
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.protection = sum(part["protection"] for part in self.armour)

        self.power += self.weapon["power"]

        if self.potion:
            self.power += self.potion["effect"].get("power", 0)
            self.hp += self.potion["effect"].get("hp", 0)
            self.protection += self.potion["effect"].get("protection", 0)

    def fight(self, opponent: "Knight") -> None:
        opponent.hp -= max(self.power - opponent.protection, 0)
        self.hp -= max(opponent.power - self.protection, 0)

        if self.hp <= 0:
            self.hp = 0
        if opponent.hp <= 0:
            opponent.hp = 0
