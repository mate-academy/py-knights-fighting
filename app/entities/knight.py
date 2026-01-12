from __future__ import annotations
from app.config.knight_config import KnightConfig


class Knight:
    def __init__(self, config: KnightConfig) -> None:
        """
        Represents a battle-ready knight with fully prepared stats. The knight
        contains health, power and armour attributes that define its combat
        behavior during duels.

        :param config: KnightConfig containing finalized knight attributes
        """
        self.name: str = config.name
        self.hp: int = config.hp
        self.power: int = config.power
        self.armour: int = config.armour

    def attack(self, other: Knight) -> None:
        """
        Performs an attack on another knight. The damage is calculated using
        the attacker's power reduced by the defender's armour. Health cannot
        be reduced below zero.

        :param other: Knight - the knight being attacked
        :return: None
        """
        damage = max(self.power - other.armour, 0)
        other.take_damage(damage)

    def take_damage(self, damage: int) -> None:
        """
        Reduces the knight's health by the given damage value and ensures
        the resulting HP does not fall below zero.

        :param damage: int - amount of damage received
        :return: None
        """
        self.hp -= damage
        self.check_health()

    def check_health(self) -> None:
        """
        Ensures the knight's health is not negative. If HP becomes
        zero or below, it is set strictly to zero.

        :return: None
        """
        if self.hp <= 0:
            self.hp = 0
