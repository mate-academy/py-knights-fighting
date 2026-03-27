from __future__ import annotations


class Knight:
    dic = dict()

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

        self.apply_armour(knight["armour"])
        self.apply_weapon(knight["weapon"])
        self.apply_potion(knight["potion"])

        self.dic[self.name] = self

    def apply_armour(self, armour: list) -> None:
        for part in armour:
            self.protection += part["protection"]

    def apply_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def apply_potion(self, potion: dict | None) -> None:
        prop_list = ["power", "protection", "hp"]

        for elem in prop_list:
            if potion is not None:
                if elem in potion["effect"]:
                    setattr(self,
                            elem,
                            getattr(self, elem) + potion["effect"][elem])

    def check_hp(self) -> None:
        if self.hp <= 0:
            self.hp = 0

    def fighting(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection
        self.check_hp()
        enemy.check_hp()
