class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def apply_armour(self, protection: int):
        if hasattr(self, "armour"):
            self.protection += protection

    def apply_weapon(self, power: int):
        self.power += power

    def apply_potion(self, effect: int):
        if effect > 0:
            self.power += effect
            self.power += effect
            self.protection += effect
        else:
            self.power -= abs(effect)
            self.power -= abs(effect)
            self.protection -= abs(effect)

