from typing import Optional


class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: Optional[dict],
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = sum(part["protection"] for part in armour)
        self.power += weapon["power"]

        if potion is not None:
            effect = potion["effect"]
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def fight(self, opponent: "Knight") -> None:
        self.hp -= opponent.power - self.protection
        opponent.hp -= self.power - opponent.protection

        if self.hp <= 0:
            self.hp = 0

        if opponent.hp <= 0:
            opponent.hp = 0
