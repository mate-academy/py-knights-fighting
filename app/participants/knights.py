class Knight:

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.opponent = None

    def opponents(self, dict_knight: dict, name1: str, name2: str) -> None:
        if self.name == name1:
            for one in dict_knight:
                other = dict_knight[one]
                if other.name == name2:
                    self.opponent = other
                    other.opponent = self

    def apply_armour(self, armour: list) -> None:
        for one in armour:
            self.protection += one["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict) -> None:
        for one in potion:
            if one == "power":
                self.power += potion["power"]
            if one == "hp":
                self.hp += potion["hp"]
            if one == "protection":
                self.protection += potion["protection"]

    def fighting(self) -> None:
        other = self.opponent
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp < 0:
            self.hp = 0
        if other.hp < 0:
            other.hp = 0
