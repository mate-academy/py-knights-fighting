from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: None | dict
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power + weapon["power"]
        self.protection = sum([i["protection"] for i in armour])

        if potion is not None:
            potion_effect = potion["effect"]
            attributes = ["power", "hp", "protection"]
            for attr in attributes:
                setattr(self,
                        attr,
                        getattr(self, attr) + potion_effect.get(attr, 0)
                        )

    def attack(self, other: Knight) -> None:
        other.hp -= (self.power - other.protection)
        self.hp -= (other.power - self.protection)
        if other.hp < 0:
            other.hp = 0
        elif self.hp < 0:
            self.hp = 0
