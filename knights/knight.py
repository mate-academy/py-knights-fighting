class Knight:

    protection = 0

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.add_armor_protection(armour)
        self.add_weapon_power(weapon)
        self.add_potion(potion)

    def add_armor_protection(self, armour: list) -> None:
        for equipment in armour:
            self.protection += equipment["protection"]

    def add_weapon_power(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def add_potion(self, potion: dict) -> None:
        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]

            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]

    def defend(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection

        if (self.hp <= 0):
            self.hp = 0
