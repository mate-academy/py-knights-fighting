"""Knight model and preparation logic."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Knight:
    """Represents a combatant with all battle modifiers applied."""

    name: str
    base_power: int
    base_hp: int
    armour: list[dict[str, Any]] = field(default_factory=list)
    weapon: dict[str, Any] | None = None
    potion: dict[str, Any] | None = None
    hp: int = 0
    power: int = 0
    protection: int = 0

    @classmethod
    def from_config(cls, raw_knight: dict[str, Any]) -> "Knight":
        knight = cls(
            name=raw_knight.get("name", ""),
            base_power=raw_knight.get("power", 0),
            base_hp=raw_knight.get("hp", 0),
            armour=raw_knight.get("armour", []),
            weapon=raw_knight.get("weapon"),
            potion=raw_knight.get("potion"),
        )
        knight.prepare_for_battle()
        return knight

    def prepare_for_battle(self) -> None:
        """Apply armour, weapon, and potion effects before combat."""
        self.protection = sum(
            armour_piece.get("protection", 0)
            for armour_piece in self.armour
        )
        self.power = self.base_power
        self.hp = self.base_hp

        if self.weapon is not None:
            self.power += self.weapon.get("power", 0)

        if self.potion is not None:
            effect = self.potion.get("effect", {})
            self.hp += effect.get("hp", 0)
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
