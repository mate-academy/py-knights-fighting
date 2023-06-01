from __future__ import annotations


class Potion:
    def __init__(self,
                 name: str,
                 change_hp: int = 0,
                 change_power: int = 0,
                 change_protection: int = 0) -> None:
        self.name = name
        self.change_hp = change_hp
        self.change_power = change_power
        self.change_protection = change_protection

    @classmethod
    def from_dict(cls, potion_dict: dict) -> Potion:
        if potion_dict:
            return cls(
                potion_dict["name"],
                potion_dict["effect"].get("hp", 0),
                potion_dict["effect"].get("power", 0),
                potion_dict["effect"].get("protection", 0)
            )
