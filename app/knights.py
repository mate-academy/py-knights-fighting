class Knight:

    def apply_potion(self, potion: dict) -> None:
        if potion is None:
            return None
        self.power += potion.get("power", 0)
        self.hp += potion.get("hp", 0)
        self.protection += potion.get("protection", 0)

    def apply_armour(self, armour: list) -> None:
        for i in armour:
            self.protection += i["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, potion: dict, weapon: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.apply_potion(potion)
        self.apply_armour(armour)
        self.apply_weapon(weapon)
