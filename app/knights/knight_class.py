from __future__ import annotations
from typing import Union


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: Union[None, dict],
            protection: int = 0
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __repr__(self) -> str:
        return f"{self.name}"

    def knight_ready_for_fight(self) -> None:

        if self.armour:
            for element in self.armour:
                added_points = element["protection"]
                element_name = element["part"]
                self.protection += added_points
                print(f"Armour {element_name} "
                      f"added {added_points} points to knight's protection.")

        self.power += self.weapon["power"]
        added_points_weapon = self.weapon["power"]
        weapon_name = self.weapon["name"]
        print(f"{weapon_name}"
              f" added {added_points_weapon} points to knight's power.")

        if self.potion is not None:

            stats = {
                "power": self.power,
                "hp": self.hp,
                "protection": self.protection
            }

            effect_name = self.potion["name"]
            stats_updates_with_effect = self.potion["effect"]

            for stat, stat_value in stats_updates_with_effect.items():
                stats[stat] += stat_value

            for stat, stat_value in stats.items():
                setattr(self, stat, stat_value)

            print(f"Potion {effect_name} is added to knight's stats.")

        print(f"CURRENT STATS OF {self.name}:")
        print(f"|power = {self.power}|"
              f"|hp = {self.hp}|"
              f"|protection = {self.protection}|")
