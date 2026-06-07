class Knight:
    def __init__(self, name: str, hp: int, power: int) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0

    def apply_armour(self, armour: dict) -> None:
        self.armour = armour
        for item in self.armour:
            self.protection += item.get("protection")

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon.get("power")

    def apply_potion(self, potion: dict) -> None:
        if potion:
            effects = potion.get("effect")
            self.protection += effects.get("protection", 0)
            self.power += effects.get("power", 0)
            self.hp += effects.get("hp", 0)

    def take_damage(self, attacker_power: int) -> None:
        damage = attacker_power - self.protection
        if damage < 0:
            damage = 0
        self.hp = max(0, self.hp - damage)
