"""Knight domain model and configuration types."""

from dataclasses import dataclass
from typing import Dict, List, Optional, TypedDict


class ArmourConfig(TypedDict):
    part: str
    protection: int


class WeaponConfig(TypedDict):
    name: str
    power: int


class PotionConfig(TypedDict):
    name: str
    effect: Dict[str, int]


class KnightConfig(TypedDict):
    name: str
    power: int
    hp: int
    armour: List[ArmourConfig]
    weapon: WeaponConfig
    potion: Optional[PotionConfig]


@dataclass
class Knight:
    """A combat-ready knight with effective battle statistics."""

    name: str
    power: int
    hp: int
    protection: int

    @classmethod
    def from_config(cls, config: KnightConfig) -> "Knight":
        """Create a combat-ready knight without changing its configuration."""
        potion = config["potion"]
        effects = {} if potion is None else potion["effect"]
        armour_protection = sum(
            armour["protection"] for armour in config["armour"]
        )

        return cls(
            name=config["name"],
            power=(
                config["power"]
                + config["weapon"]["power"]
                + effects.get("power", 0)
            ),
            hp=config["hp"] + effects.get("hp", 0),
            protection=(
                armour_protection + effects.get("protection", 0)
            ),
        )

    def receive_attack(self, opponent_power: int) -> None:
        """Apply one attack and clamp defeated knights' HP to zero."""
        self.hp = max(0, self.hp - (opponent_power - self.protection))
