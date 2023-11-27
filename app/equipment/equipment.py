from typing import Any


class Equipment:
    def __init__(self, weapon_power: int, armour: list) -> None:
        self.weapon_power = weapon_power
        self.armour = armour

    def apply_armour(self, knight: Any) -> None:
        knight.protection = 0
        for part in self.armour:
            knight.protection += part["protection"]

    def apply_weapon(self, knight: Any) -> None:
        knight.power += self.weapon_power

    def apply_potion(self, knight: Any) -> None:
        if knight.potion is not None:
            for effect, points in knight.potion["effect"].items():
                if effect == "power":
                    knight.power += points
                if effect == "protection":
                    knight.protection += points
                if effect == "hp":
                    knight.health_points += points
