from __future__ import annotations

from app.items.armour import Armour
from app.items.weapon import Weapon
from app.items.potion import Potion


class Knight:
    """
    Represents a knight in the battle. Each knight has health points (hp),
    power, and protection which can be affected by armour,
    weapons, and potions.

    Attributes:
        name (str): The name of the knight.
        hp (int): Health points of the knight.
        power (int): Base power of the knight.
        protection (int): The knight's defense value against attacks.
        armour (list[Armour]): List of armour pieces the knight wears.
        weapon (Weapon): The knight's weapon.
        potion (Potion): Potion that can affect the knight's stats.
    """

    def __init__(self, name: str, power: int, hp: int) -> None:
        """
        Initializes the knight with a name, base power, and health points.
        Protection is set to 0 by default.

        Args:
            name (str): The name of the knight.
            power (int): The base power of the knight.
            hp (int): The initial health points of the knight.
        """
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = 0
        self.armour: list[Armour] = []
        self.weapon: Weapon = None
        self.potion: Potion = None

    def set_protection(self, armours: list[Armour]) -> None:
        """
        Sets the knight's protection value
        by summing up the protection from all armour pieces.

        Args:
            armours (list[Armour]):
                List of armour pieces that provide protection.
        """
        self.protection += sum(armour.protection for armour in armours)

    def increase_power(self, weapon: Weapon) -> None:
        """
        Increases the knight's power by the weapon's power.

        Args:
            weapon (Weapon): The knight's weapon that increases power.
        """
        self.power += weapon.power

    def set_effect(self, potion: Potion) -> None:
        """
        Applies a potion's effect to the knight's stats:
            (hp, power, and protection).

        Args:
            potion (Potion): The potion that affects the knight's stats.
        """
        if potion:
            self.hp += potion.effect.get("hp", 0)
            self.power += potion.effect.get("power", 0)
            self.protection += potion.effect.get("protection", 0)

    def fight(self, opponent: Knight) -> None:
        """
        Simulates a battle round between this knight
        and an opponent by reducing
        their HP based on the opponent's power and their own protection.

        Args:
            opponent (Knight): The opponent knight to fight against.
        """
        self.hp = max(self.hp - (opponent.power - self.protection), 0)
        opponent.hp = max(opponent.hp - (self.power - opponent.protection), 0)
