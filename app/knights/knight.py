from typing import Any


class Knight:
    """Represents a knight with hp, power,
    protection, armour, weapon and potion."""

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict[str, str | int]],
                 weapon: dict[str, str | int],
                 potion: dict[str, Any] | None
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare(self) -> None:
        """Apply armour, weapon and potion
        effects to update stats."""

        # Apply armour
        self.protection = sum(a["protection"] for a in self.armour)

        # Apply weapon
        self.power += self.weapon["power"]

        # Apply potion
        if self.potion:
            for stat, value in self.potion["effect"].items():
                setattr(self, stat, getattr(self, stat) + value)

    def attack(self, other_knight: "Knight") -> None:
        """Attack another knight, reducing
        their HP based on power & protection."""

        other_knight.hp -= self.power - other_knight.protection
        other_knight.hp = max(0, other_knight.hp)
