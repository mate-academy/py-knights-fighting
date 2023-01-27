from __future__ import annotations


class KnightFighter:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict[str, int]] = None,
            weapon: dict[dict[str, int]] = None,
            potion: dict[dict[dict[str, int]]] = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def fight(self, opponent: KnightFighter) -> None:
        self.hp = self.hp - (opponent.power - self.armour)
        self.hp = 0 if self.hp < 0 else self.hp
