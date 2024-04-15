from __future__ import annotations


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.protection = 0

    def get_potion(self, potion: dict | None) -> None:
        if potion is not None and "effect" in potion:
            potion_effect = potion["effect"]
            if "power" in potion_effect:
                self.power += potion_effect["power"]
            if "hp" in potion_effect:
                self.hp += potion_effect["hp"]
            if "protection" in potion_effect:
                self.protection += potion_effect["protection"]

    def get_armour(self, armour: list[dict] | None) -> None:
        sum_armour = sum(arm["protection"] for arm in armour)
        self.protection += sum_armour

    def get_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def get_upgrade(self, knight: dict) -> None:
        self.get_potion(knight["potion"])
        self.get_weapon(knight["weapon"])
        self.get_armour(knight["armour"])

    def fight(self, knight: Knight) -> None:
        self.hp -= knight.power - self.protection
        if self.hp <= 0:
            self.hp = 0
