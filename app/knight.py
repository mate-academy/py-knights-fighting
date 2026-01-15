from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict | None = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = self.calculate_protection()
        self.use_potion()

    def calculate_protection(self) -> int:
        return sum(armour_part["protection"] for armour_part in self.armour)

    def use_potion(self) -> None:
        if self.potion:
            effect_names = self.potion["effect"].keys()
            for key in effect_names:
                setattr(
                    self, key, getattr(self, key) + self.potion["effect"][key]
                )

    def attack(self, opponent: Knight) -> None:
        damage = self.power + self.weapon["power"] - opponent.protection
        opponent.hp -= damage
        if opponent.hp < 0:
            opponent.hp = 0
