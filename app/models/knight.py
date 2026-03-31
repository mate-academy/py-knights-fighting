from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            base_power: int,
            hp: int,
            armour: list[dict],
            weapon: dict,
            potion: dict | None
    ) -> None:
        self.name = name
        self.base_power = base_power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.power = 0

    @classmethod
    def from_dict(cls, dictionary: dict) -> Knight:
        return Knight(
            dictionary["name"],
            dictionary["power"],
            dictionary["hp"],
            dictionary["armour"],
            dictionary["weapon"],
            dictionary["potion"])

    def prepare(self) -> None:
        self.power = self.base_power + self.weapon["power"]
        self.protection = sum(
            [armor_piece["protection"] for armor_piece in self.armour])

        if self.potion:
            effect = self.potion["effect"]
            self.protection += effect.get("protection", 0)
            self.power += effect.get("power", 0)
            self.hp += effect.get("hp", 0)
