from __future__ import annotations


class Potion:
    def __init__(
        self,
        name: str,
        hp_adj: int = 0,
        power_adj: int = 0,
        protection_adj: int = 0,
    ) -> None:
        self.name = name
        self.hp_adj = hp_adj
        self.power_adj = power_adj
        self.protection_adj = protection_adj

    @classmethod
    def from_dict(cls, dct: dict) -> Potion:
        effects = dct["effect"]
        return cls(
            dct["name"],
            effects.get("hp", 0),
            effects.get("power", 0),
            effects.get("protection", 0),
        )
