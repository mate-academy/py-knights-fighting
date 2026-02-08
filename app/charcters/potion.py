from __future__ import annotations


class Potion:
    def __init__(
        self,
        name: str,
        power: int = 0,
        hp: int = 0,
        protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def __str__(self) -> str:
        return (
            f"Potion({self.name}, effect: power={self.power}, "
            f"hp={self.hp}, protection={self.protection})"
        )
