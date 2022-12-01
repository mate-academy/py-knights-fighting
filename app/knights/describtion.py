from __future__ import annotations

from app.additional_config.wepon import Weapon
from app.additional_config.protection import Armour


class Characteristics:

    def __init__(self, hp: int, power: int, protection: int = 0) -> None:
        self.hp = hp
        self.power = power
        self.protection = protection

    def basic_knights_config(self, weapon: int, armour: list = None) -> dict:
        weapon = Weapon(weapon["power"])
        self.power += weapon.power_weapon
        before_battle_stats = {"hp": self.hp, "power": self.power}

        # apply protection
        total_protection = 0
        if len(armour) != 0:
            for arm in armour:
                armour = Armour(arm["protection"])
                total_protection = armour + total_protection
                before_battle_stats.update({"protection":
                                           total_protection.protection_armour
                                            })
        else:
            before_battle_stats.update({"protection": 0})

        return before_battle_stats
