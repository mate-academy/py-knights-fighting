from __future__ import annotations


class Knight:

    def __init__(self, knight_dict: dict) -> None:
        self.dict = knight_dict
        self.name = self.dict["name"]
        self.power = self.dict["power"]
        self.hp = self.dict["hp"]
        self.weapon = self.dict["weapon"]
        self.protection = 0
        self.potion()
        self.armour()
        self.weapons()

    def potion(self) -> None:
        if self.dict["potion"] is not None:

            for effect in self.dict["potion"]["effect"]:

                if effect == "hp":
                    self.hp += self.dict["potion"]["effect"]["hp"]

                if effect == "power":
                    self.power += self.dict["potion"]["effect"]["power"]

                if effect == "protection":
                    self.protection += \
                        self.dict["potion"]["effect"]["protection"]

    def armour(self) -> None:
        if self.dict["armour"]:

            for part in self.dict["armour"]:
                self.protection += part["protection"]

    def weapons(self) -> None:
        self.power += self.dict["weapon"]["power"]

    def fight(self, enemy: Knight) -> None:
        self.hp -= enemy.power - self.protection
        enemy.hp -= self.power - enemy.protection

        if self.hp <= 0:
            self.hp = 0

        if enemy.hp <= 0:
            enemy.hp = 0
