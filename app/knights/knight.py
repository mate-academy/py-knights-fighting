from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,

    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def prepare(
            self,
            armour: list[dict],
            weapon: dict,
            potion: dict
    ) -> None:
        if armour is not None:
            for item in armour:
                self.protection += item["protection"]

        self.power += weapon["power"]

        if potion is not None and "effect" in potion:
            effects = potion["effect"]
            for effect_type, value in effects.items():
                if effect_type == "power":
                    self.power += value
                elif effect_type == "hp":
                    self.hp += value
                elif effect_type == "protection":
                    self.protection += value

    def perform_combat(self, opponent: Knight) -> None:
        self.hp -= max(opponent.power - self.protection, 0)
        opponent.hp -= max(self.power - opponent.protection, 0)

    def __str__(self) -> str:
        return (f"{self.name}: - HP: {self.hp},"
                f" Power: {self.power},"
                f" Protection: {self.protection}")
