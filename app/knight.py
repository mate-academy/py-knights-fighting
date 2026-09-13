"""Knight model and the battle logic between two knights."""

from dataclasses import dataclass
from typing import Optional, Type


@dataclass
class Knight:
    name: str
    hp: int
    power: int
    protection: int = 0

    @classmethod
    def from_config(cls: Type["Knight"], config: dict) -> "Knight":
        """Build a battle-ready Knight from a raw KNIGHTS config entry."""
        knight = cls(
            name=config["name"],
            hp=config["hp"],
            power=config["power"],
        )
        knight._wear_armour(config.get("armour") or [])
        knight._wield_weapon(config["weapon"])
        knight._drink_potion(config.get("potion"))
        return knight

    def _wear_armour(self: "Knight", armour: list) -> None:
        self.protection += sum(piece["protection"] for piece in armour)

    def _wield_weapon(self: "Knight", weapon: dict) -> None:
        self.power += weapon["power"]

    def _drink_potion(self: "Knight", potion: Optional[dict]) -> None:
        if not potion:
            return
        effect = potion["effect"]
        self.hp += effect.get("hp", 0)
        self.power += effect.get("power", 0)
        self.protection += effect.get("protection", 0)

    def receive_hit(self: "Knight", attack_power: int) -> None:
        """Reduce hp by incoming power minus own protection (min 0)."""
        self.hp = max(self.hp - (attack_power - self.protection), 0)


def fight(first: Knight, second: Knight) -> dict:
    """Simulate one simultaneous exchange of blows between two knights."""
    first_power, second_power = first.power, second.power
    first.receive_hit(second_power)
    second.receive_hit(first_power)
    return {first.name: first.hp, second.name: second.hp}
