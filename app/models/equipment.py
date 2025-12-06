from __future__ import annotations
from typing import Optional


class ArmourPiece:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class PotionEffect:
    def __init__(self, hp: int = 0,
                 power: int = 0, protection: int = 0) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    @classmethod
    def create_from_dict(cls, data: dict) -> PotionEffect:
        if not data:
            return cls()
        return cls(
            hp=data.get("hp", 0),
            power=data.get("power", 0),
            protection=data.get("protection", 0)
        )


class Potion:
    def __init__(self, name: str, effect: PotionEffect) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def create_from_dict(cls, data: dict | None) -> Optional[Potion]:
        if not data:
            return None
        effect = PotionEffect.create_from_dict(data.get("effect", {}))
        return cls(name=data["name"], effect=effect)
