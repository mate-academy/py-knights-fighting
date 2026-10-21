"""Domain models used in the knights battle simulation."""

from typing import Optional


class Armour:
    """One piece of armour (helmet, boots, etc.)."""

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    """A weapon a knight fights with."""

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    """A potion that boosts or weakens a knight before battle."""

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Knight:
    """A single knight taking part in the tournament."""

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: Weapon,
        potion: Optional[Potion] = None,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

    def prepare_for_battle(self) -> None:
        """Put on armour and weapon, drink the potion (if any)."""
        self.protection = sum(item.protection for item in self.armour)
        self.power += self.weapon.power

        if self.potion is not None:
            effect = self.potion.effect
            self.power += effect.get("power", 0)
            self.protection += effect.get("protection", 0)
            self.hp += effect.get("hp", 0)

    def fight(self, opponent: "Knight") -> None:
        """Exchange hits with an opponent at the same time."""
        my_damage = opponent.power - self.protection
        opponent_damage = self.power - opponent.protection

        self.hp -= my_damage
        opponent.hp -= opponent_damage

        self.hp = max(self.hp, 0)
        opponent.hp = max(opponent.hp, 0)
