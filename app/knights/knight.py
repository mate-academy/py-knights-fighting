from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Knight:
    """Represents a knight ready for battle, stats already applied."""

    name: str
    power: int
    hp: int
    protection: int = 0

    @classmethod
    def from_config(cls, config: dict) -> "Knight":
        protection = sum(
            item["protection"] for item in config["armour"]
        )
        power = config["power"] + config["weapon"]["power"]
        hp = config["hp"]

        potion = config.get("potion")
        if potion is not None:
            effect = potion["effect"]
            power += effect.get("power", 0)
            protection += effect.get("protection", 0)
            hp += effect.get("hp", 0)

        return cls(
            name=config["name"], power=power, hp=hp, protection=protection
        )

    def receive_damage(self, opponent_power: int) -> None:
        self.hp -= opponent_power - self.protection
        if self.hp <= 0:
            self.hp = 0

    @property
    def is_defeated(self) -> bool:
        return self.hp <= 0
