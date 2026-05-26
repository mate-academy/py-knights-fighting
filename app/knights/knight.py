class Knight:
    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: dict | None) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        self.apply_armor()
        self.apply_weapon()
        self.apply_potion()

    def apply_armor(self) -> None:
        for piece_of_armor in self.armour:
            self.protection += piece_of_armor["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            effects = self.potion["effect"]
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)

    def battle(self, opponent: "Knight") -> None:
        self.hp -= max(0, opponent.power - self.protection)
        opponent.hp -= max(0, self.power - opponent.protection)

        self.hp = max(0, self.hp)
        opponent.hp = max(0, opponent.hp)
