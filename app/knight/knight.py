from __future__ import annotations
from typing import Optional, Dict


class Knight:
    def __init__(
            self, knight_config: Dict, potion: Optional[Dict] = None
    ) -> None:
        self.knight_config = knight_config
        self.potion = potion


def get_power_of_knight(knight: Knight) -> int:
    power = knight.knight_config["power"]
    weapon_power = knight.knight_config["weapon"]["power"]
    # If potion is?
    if (knight.potion and "effect" in knight.potion
            and "power" in knight.potion["effect"]):
        return power + weapon_power + knight.potion["effect"]["power"]
    return power + weapon_power


def get_protection_of_knight(knight: Knight) -> int:
    armour = knight.knight_config["armour"]
    total_protection = sum([equip["protection"] for equip in armour])
    # If potion is?
    if (knight.potion and "effect" in knight.potion
            and "protection" in knight.potion["effect"]):
        return total_protection + knight.potion["effect"]["protection"]
    return total_protection


def get_hp_of_knight(knight: Knight) -> int:
    hp = knight.knight_config["hp"]
    # If potion is?
    if (knight.potion and "effect" in knight.potion
            and "hp" in knight.potion["effect"]):
        return hp + knight.potion["effect"]["hp"]
    return hp
