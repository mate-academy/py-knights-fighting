from __future__ import annotations


class Armor:

    def __init__(self, part: str, protection: int = 0) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(
            self,
            name: str = "Unknown",
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int = 0) -> None:
        self.name = name
        self.power = power


class Knight:

    def __str__(self) -> str:
        return (f"Knight(name: {self.name}, "
                f"total_power: {self.total_power}, "
                f"total_protection: {self.total_protection}, "
                f"current_hp: {self.current_hp})")

    def __init__(
            self,
            name: str,
            armor: [Armor],
            weapon: Weapon,
            potion: Potion,
            power: int = 0,
            hp: int = 0,
    ) -> None:
        # init params
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        # battle params
        self.current_hp = self.hp + potion.hp
        self.total_power = self.power + potion.power + weapon.power
        self.total_protection = (sum([armor_item.protection
                                     for armor_item in self.armor])
                                 + potion.protection)

    def is_dead(self) -> bool:
        return self.current_hp <= 0

    def hit_opponent(self, opponent: Knight) -> None:
        opponent.current_hp = max(
            opponent.current_hp - max(
                self.total_power - opponent.total_protection, 0
            ),
            0
        )
