from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Knight:
    name: str
    power: int
    hp: int
    armour: List[Dict[str, Any]]
    weapon: Dict[str, Any]
    potion: Optional[Dict[str, Any]] = None
    protection: int = 0

    @classmethod
    def from_config(cls, config: Dict[str, Any]) -> "Knight":
        """Tworzy obiekt Knight na podstawie słownika konfiguracyjnego."""
        return cls(
            name=config["name"],
            power=config["power"],
            hp=config["hp"],
            armour=config.get("armour", []),
            weapon=config["weapon"],
            potion=config.get("potion"),
        )

    def prepare_for_battle(self) -> None:
        """Nakłada zbroję, broń i miksturę (jeśli jest)."""
        # armour
        self.protection = sum(piece["protection"] for piece in self.armour)

        # weapon
        self.power += self.weapon["power"]
        if self.potion:
            effect = self.potion.get("effect", {})
            for stat, delta in effect.items():
                if hasattr(self, stat):
                    current_value = getattr(self, stat)
                    setattr(self, stat, current_value + delta)
