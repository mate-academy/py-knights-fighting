from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    protection: int = 0

    @classmethod
    def from_config(cls, cfg: dict[str, Any]) -> "Knight":
        name = cfg["name"]
        power = int(cfg["power"])
        hp = int(cfg["hp"])
        protection = 0

        for part in cfg.get("armour", []) or []:
            protection += int(part.get("protection", 0))

        weapon = cfg.get("weapon")
        if weapon:
            power += int(weapon.get("power", 0))

        potion = cfg.get("potion")
        if potion:
            effect = potion.get("effect", {}) or {}
            hp += int(effect.get("hp", 0))
            power += int(effect.get("power", 0))
            protection += int(effect.get("protection", 0))

        return cls(name=name, power=power, hp=hp, protection=protection)
