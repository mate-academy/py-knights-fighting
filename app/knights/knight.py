class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: str, weapon: str, potion: str) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.potion_protection = 0

    def __str__(self) -> None:
        return f"{self.name}(HP: {self.hp}, Power: {self.power})"

    def attack(self, opponent: str) -> None:
        damage = self.power + self.weapon.power - opponent.protection
        opponent.hp -= damage if damage > 0 else 0
        if opponent.hp < 0:
            opponent.hp = 0

    @property
    def protection(self) -> None:
        return sum(a.protection for a in self.armour)

    def apply_potion(self) -> None:
        if self.potion:
            if self.potion.effect.get("hp"):
                self.hp += self.potion.effect.get("hp")
            if self.potion.effect.get("power"):
                self.power += self.potion.effect.get("power")
            if self.potion.effect.get("protection"):
                self.potion_protection += self.potion.effect.get("protection")
