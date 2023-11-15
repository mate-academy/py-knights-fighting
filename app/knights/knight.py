from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list[dict[str]] | dict[str],
            weapon: dict[str],
            potion: dict[str] | None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        if isinstance(self.armour, list):
            total_protection = sum(piece["protection"]
                                   for piece in self.armour
                                   )
            self.protection = total_protection
        else:
            self.protection = self.armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            for stat, value in self.potion["effect"].items():
                setattr(
                    self,
                    stat,
                    getattr(self, stat) + value
                )

    def __str__(self) -> str:
        return (f"{self.name}: - HP: {self.hp},"
                f" Power: {self.power},"
                f" Protection: {self.protection}"
                )
