class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:

        self.name = name
        self.power = power
        self.hp = hp

        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.protection = 0
        self.apply_stats()

    def apply_stats(self) -> None:

        self.protection = sum(part["protection"] for part in self.armour)
        self.power += self.weapon["power"]

        if self.potion:
            effects = self.potion.get("effect", {})
            self.hp += effects.get("hp", 0)
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            if self.hp < 0:
                self.hp = 0

    def take_damage(self, opponent: int) -> None:
        damage = opponent.power - self.protection
        if damage > 0:
            self.hp -= damage
        if self.hp < 0:
            self.hp = 0
