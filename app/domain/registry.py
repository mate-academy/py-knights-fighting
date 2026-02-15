from __future__ import annotations
from dataclasses import dataclass
from typing import Mapping

from items import Weapon, Armour, Potion

@dataclass(frozen=True, slots=True)
class ItemRegistry:
    weapons: Mapping[str, Weapon]
    armours: Mapping[str, Armour]
    potions: Mapping[str, Potion]

@dataclass(frozen=True, slots=True)
class Loadout:
    weapon_id: str
    armour_ids: list[str]
    potion_id: str | None = None