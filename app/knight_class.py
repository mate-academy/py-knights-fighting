from __future__ import annotations


class Knight:

    def __init__(self, parameters: dict) -> None:
        self.name = parameters.get("name")
        self.power = parameters.get("power")
        self.hp = parameters.get("hp")
        self.armour = parameters.get("armour")
        self.weapon = parameters.get("weapon")
        self.potion = parameters.get("potion")
        self.protection = 0
        self.battle_preparations()
        self.parameters = parameters

    def add_potion(self) -> None:
        if self.potion:
            for key, value in self.potion["effect"].items():
                setattr(self, key, getattr(self, key) + value)

    def grab_weapon(self) -> None:
        self.power += self.weapon["power"]

    def wear_armour(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]

    def battle_preparations(self) -> None:
        self.wear_armour()
        self.grab_weapon()
        self.add_potion()

    def fight(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        if self.hp <= 0:
            self.hp = 0

    def show_hp(self) -> dict:
        return {self.name: self.hp}

    @staticmethod
    def return_result(knights: list[Knight]) -> dict:
        result = {}
        for part in knights:
            result.update(part.show_hp())
        return result
