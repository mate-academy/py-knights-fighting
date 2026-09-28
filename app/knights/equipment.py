from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Armour:
    part: str
    protection: int

    @classmethod
    def from_dict(cls, data: dict) -> Armour:
        return cls(part=data["part"], protection=data["protection"])


@dataclass(frozen=True)
class Weapon:
    name: str
    power: int

    @classmethod
    def from_dict(cls, data: dict) -> Weapon:
        return cls(name=data["name"], power=data["power"])


@dataclass(frozen=True)
class Potion:
    name: str
    effect: dict[str, int] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict | None) -> Potion | None:
        if data is None:
            return None
        return cls(name=data["name"], effect=dict(data["effect"]))
