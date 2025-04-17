from __future__ import annotations


class Knights:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict | list,
                 potion: None | dict) -> None:
        self.name = name
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.power = power + self.add_power() + self.potion_benefits()[0]
        self.hp = hp + self.potion_benefits()[1]
        self.protection = self.count_protection() + self.potion_benefits()[2]

    def count_protection(self) -> int:
        result = 0
        if self.armour:
            for part in self.armour:
                result += part.get("protection")
        return result

    def add_power(self) -> None:
        if self.weapon:
            return self.weapon["power"]
        return 0

    def potion_benefits(self) -> list:
        add_power = 0
        add_hp = 0
        add_protection = 0
        if self.potion:
            if "power" in self.potion["effect"]:
                add_power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                add_hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                add_protection += self.potion["effect"]["protection"]
        return [add_power, add_hp, add_protection]

    def battle(self, other_knights: Knights) -> None:
        self.hp -= other_knights.power - self.protection
        other_knights.hp -= self.power - other_knights.protection

        if self.hp <= 0:
            self.hp = 0

        if other_knights.hp <= 0:
            other_knights.hp = 0
