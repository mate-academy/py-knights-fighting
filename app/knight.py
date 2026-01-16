from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    @classmethod
    def from_dict(cls, data: dict) -> Knight:
        return cls(
            name=data["name"],
            power=data["power"],
            hp=data["hp"],
            armour=data.get("armour", []),
            weapon=data["weapon"],
            potion=data.get("potion")
        )

    def use_power_ups(self) -> None:
        self.protection = sum(a["protection"] for a in self.armour)
        self.power += self.weapon["power"]
        if self.potion:
            effect = self.potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def fight(self, opponent: Knight) -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection
        self.hp = max((0, self.hp))
        opponent.hp = max((0, opponent.hp))
