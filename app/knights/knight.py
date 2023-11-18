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

        if potion is not None:
            if "power" in potion["effect"]:
                self.power += potion["effect"]["power"]
            if "hp" in potion["effect"]:
                self.hp += potion["effect"]["hp"]
            if "protection" in potion["effect"]:
                self.protection += potion["effect"]["protection"]

    def perform_combat(self, opponent: Knight) -> None:
        self.hp -= max(opponent.power - self.protection, 0)
        opponent.hp -= max(self.power - opponent.protection, 0)

    def __str__(self) -> str:
        return (f"{self.name}: - HP: {self.hp},"
                f" Power: {self.power},"
                f" Protection: {self.protection}")
