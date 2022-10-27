class Knight:
    def __init__(self, name: str, power: int, hp: int, protection = 0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def apply_armor(self, armor: list):
        for item in armor:
            self.protection += item["protection"]

    def apply_weapon(self, weapon: dict):
        self.power += weapon["power"]

    def apply_potion(self, potion_name: str):
        if potion_name == "Blessing":
            self.power += 5
            self.hp += 10

        if potion_name == "Berserk":
            self.power += 15
            self.hp += -5
            self.protection += 10
