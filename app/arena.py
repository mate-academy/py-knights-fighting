# app/arena.py
from __future__ import annotations
from typing import Dict, List
from .entities import ArmorPiece, Weapon, Potion, Knight


def build_knight(raw: Dict) -> Knight:

    armour_list: List[ArmorPiece] = [
        ArmorPiece(part=a["part"], protection=a["protection"])
        for a in raw.get("armour", [])
    ]

    weapon_raw = raw.get("weapon")
    if weapon_raw is not None:
        weapon = Weapon(
            name=weapon_raw["name"],
            power=weapon_raw["power"],
        )
    else:
        weapon = None

    potion_raw = raw.get("potion")
    potion = Potion(
        name=potion_raw["name"],
        effect=potion_raw["effect"],
    ) if potion_raw else None

    return Knight(
        name=raw["name"],
        base_hp=raw["hp"],
        base_power=raw["power"],
        armour=armour_list,
        weapon=weapon,
        potion=potion,
    )


def duel_stats(k1: Knight, k2: Knight) -> Dict[str, int]:

    s1 = k1.final_stats()
    s2 = k2.final_stats()

    hp1_after = s1["hp"] - (s2["power"] - s1["protection"])
    hp2_after = s2["hp"] - (s1["power"] - s2["protection"])

    if hp1_after <= 0:
        hp1_after = 0
    if hp2_after <= 0:
        hp2_after = 0

    return {
        k1.name: hp1_after,
        k2.name: hp2_after,
    }
