from __future__ import annotations

from app.config.battlekit import BattleKit


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            battle_kit: BattleKit = None
    ) -> None:
        """
        Constructor for the Knight class

        This constructor initializes a Knight object
        with provided attributes and an optional battle kit
        """
        self.name = name
        self.power = power
        self.hp = hp
        self.battle_kit = battle_kit
        self.protection = 0

    def apply_potion(self) -> None:
        """
        Apply the effects of the knight's equipped potion

        This method applies the effects of the knight's potion
        to the knight's attributes
        """
        if self.battle_kit.potion.name is not None:
            for effect, value in self.battle_kit.potion.effect.items():
                if effect == "power":
                    self.power += value
                elif effect == "hp":
                    self.hp += value
                elif effect == "protection":
                    self.protection += value

    def equip(self, battle_kit: BattleKit) -> None:
        """
        Equip the knight with a battle kit

        This method equips the knight with a provided
        battle kit and adjusts attributes accordingly
        """
        self.battle_kit = battle_kit
        self.power += battle_kit.weapon.power
        self.apply_potion()

        if battle_kit.armour is not None:
            for item in battle_kit.armour:
                self.protection += item.protection

    def battle(self, other: Knight) -> dict:
        """
        Simulate a battle between two knights

        Args:
            other (Knight):
                The opponent knight.

        Returns:
            dict:
                A dictionary containing the
                updated hit points of both knights.

        This method simulates a battle between two knights
        and updates their hit points.
        """
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0

        return {
            self.name: self.hp,
            other.name: other.hp
        }
