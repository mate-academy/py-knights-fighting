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
    potion_power = knight.potion.get("effect", {}).get("power", 0) \
        if knight.potion else 0
    return power + weapon_power + potion_power


def get_protection_of_knight(knight: Knight) -> int:
    total_protection = sum(
        equip["protection"] for equip in knight.knight_config["armour"]
    )
    potion_protection = knight.potion.get("effect", {}).get("protection", 0) \
        if knight.potion else 0
    return total_protection + potion_protection


def get_hp_of_knight(knight: Knight) -> int:
    hp = knight.knight_config["hp"]
    potion_hp = knight.potion.get("effect", {}).get("hp", 0) \
        if knight.potion else 0
    return hp + potion_hp
