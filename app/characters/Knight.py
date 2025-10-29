from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict, potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @staticmethod
    def create_character(stats: dict) -> Knight:
        return Knight(name=stats["name"], power=stats["power"], hp=stats["hp"],
                      armour=stats["armour"], weapon=stats["weapon"],
                      potion=stats["potion"])

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if not self.potion:
            return

        effect = self.potion["effect"]
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)
        self.hp += effect.get("hp", 0)
