class Knight:
    def __init__(self, name: str, power: int, hp: int, armour, weapon, potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.potion_protection = 0

    def __str__(self):
        return f"{self.name}(HP: {self.hp}, Power: {self.power})"

    def attack(self, opponent):
        damage = self.power + self.weapon.power - opponent.protection
        opponent.hp -= damage if damage > 0 else 0
        if opponent.hp < 0:
            opponent.hp = 0

    @property
    def protection(self):
        return sum(a.protection for a in self.armour)

    def apply_potion(self):
        if self.potion:
            if self.potion.effect.get("hp"):
                self.hp += self.potion.effect.get("hp")
            if self.potion.effect.get("power"):
                self.power += self.potion.effect.get("power")
            if self.potion.effect.get("protection"):
                self.potion_protection += self.potion.effect.get("protection")


class Weapon:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name} (+{self.power} Power)"

class Armour:
    def __init__(self, part, protection):
        self.part = part
        self.protection = protection

    def __str__(self):
        return f"{self.part} (+{self.protection} Protection)"

class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def __str__(self):
        return f"{self.name} ({self.effect})"
