from typing import Dict


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def from_dict(cls, data: Dict) -> "Weapon":
        return cls(name=data["name"], power=data["power"])


class ArmourPart:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_dict(cls, data: Dict) -> "ArmourPart":
        return cls(part=data["part"], protection=data["protection"])


class Potion:
    def __init__(self, name: str, hp: int = 0, power: int = 0,
                 protection: int = 0) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection

    @classmethod
    def from_dict(cls, data: Dict) -> "Potion":
        effect = data.get("effect", {})
        return cls(
            name=data["name"],
            hp=effect.get("hp", 0),
            power=effect.get("power", 0),
            protection=effect.get("protection", 0),
        )
