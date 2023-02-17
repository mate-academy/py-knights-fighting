from __future__ import annotations


class Knight:

    def __init__(self, knight_dict: dict) -> None:
        self.name = knight_dict["name"]

        self.armour = knight_dict["armour"]
        self.weapon = knight_dict["weapon"]
        self.potion = knight_dict["potion"]

        self.hp = knight_dict["hp"]
        self.power = knight_dict["power"] + self.weapon["power"]
        self.protection = 0

        for arm in self.armour:
            self.protection += arm["protection"]

        if self.potion is not None:
            characteristics_list = ["power", "protection", "hp"]
            for characteristic in characteristics_list:
                if characteristic in self.potion["effect"]:
                    setattr(self,
                            characteristic,
                            getattr(self, characteristic)
                            + self.potion["effect"][characteristic])

    def duel(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        def check_hp(hp: int) -> int:
            if hp <= 0:
                hp = 0
            return hp

        self.hp = check_hp(self.hp)
        enemy.hp = check_hp(enemy.hp)
