from __future__ import annotations
from dataclasses import dataclass

from app.domain.items import Weapon, Armour, Potion
from app.domain.registry import ItemRegistry, Loadout


@dataclass(slots=True)
class Knight:
    name: str
    hp: int
    power: int
    protection: int
    registry: ItemRegistry
    equipment: Loadout

    @property
    def weapon(self) -> Weapon:
        return self.registry.weapons[self.equipment.weapon_id]

    @property
    def armour(self) -> list[Armour]:
        return [
            self.registry.armours[a_id]
            for a_id in self.equipment.armour_ids
        ]

    @property
    def potion(self) -> Potion | None:
        if self.equipment.potion_id is None:
            return None
        return self.registry.potions[self.equipment.potion_id]

    def apply_equipment(self) -> Combatant:
        potion = self.potion

        hp_bonus = potion.effect.get("hp", 0) if potion else 0
        potion_power = potion.effect.get("power", 0) if potion else 0
        potion_protection = potion.effect.get("protection", 0) if potion else 0

        weapon_power = self.weapon.power
        protection_bonus = (sum(a.strength for a in self.armour)
                            + potion_protection)

        hp = self.hp + hp_bonus
        power = self.power + weapon_power + potion_power
        protection = self.protection + protection_bonus

        return Combatant(self.name, hp, power, protection)


@dataclass(slots=True)
class Combatant:
    name: str
    hp: int
    power: int
    protection: int
