class Knight:

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

        self.add_armor_protection(armour)
        self.add_weapon_power(weapon)
        self.add_potion(potion)

    def add_armor_protection(self, armour: list) -> None:
        for equipment in armour:
            self.protection += equipment["protection"]

    def add_weapon_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def add_potion(self, potion: dict) -> None:
        if potion:
            effect = potion.get("effect", {})
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def defend(self, opponent: Knight) -> None:
        damage = opponent.power - self.protection
        if damage > 0:
            self.hp -= damage

        if self.hp < 0:
            self.hp = 0
