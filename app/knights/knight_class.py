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

        print("                                        ")
        print(f"{self.name} is getting ready for the fight.")
        print("                                        ")

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

            effect_name = self.potion["name"]
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]
            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]
            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]
            print(f"Potion {effect_name} is added to knight's stats.")
            print("                                        ")

        print(f"CURRENT STATS OF {self.name}:")
        print(f"|power = {self.power}"
              f"|hp = {self.hp}"
              f"|protection = {self.protection}|")
        print("                                        ")
        print(f"Knight {self.name} is ready for the fight.")
        print("___________________________________________")
