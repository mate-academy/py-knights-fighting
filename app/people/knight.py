from __future__ import annotations


class Knight:
    def __init__(self, config: dict) -> None:
        self.name = config["name"]
        self.power = config["power"] + config["weapon"]["power"]
        self.hp = config["hp"]
        self._apply_armour(armour=config["armour"])
        if config["potion"]:
            self._apply_potion(potion=config["potion"])

    def _apply_armour(self, armour: list[dict]) -> None:
        self.protection = 0
        for element in armour:
            self.protection += element["protection"]

    def _apply_potion(self, potion: dict) -> None:
        attributes = ["power", "protection", "hp"]
        for attribute in attributes:
            if attribute in potion["effect"]:
                self.__dict__[attribute] += potion["effect"][attribute]

    def __isub__(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        if self.hp < 0:
            self.hp = 0
        return self

    def fight_with(self, knight: Knight) -> dict:
        self -= knight
        knight -= self
        return {
            self.name: self.hp,
            knight.name: knight.hp
        }
