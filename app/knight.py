from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict | None,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def preparations(self) -> None:
        for item in self.armour:
            self.protection += item["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            self.power += self.potion["effect"].get("power", 0)
            self.protection += self.potion["effect"].get("protection", 0)
            self.hp += self.potion["effect"].get("hp", 0)

    def battle_result(self, opposition: Knight) -> dict:
        self.hp -= opposition.power - self.protection
        opposition.hp -= self.power - opposition.protection

        return {self.name: max(self.hp, 0),
                opposition.name: max(opposition.hp, 0)}
