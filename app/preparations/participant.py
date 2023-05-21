from __future__ import annotations

from .extras import Armor, Weapon, Potion


class Participant:
    people = {}
    fighters = []

    @classmethod
    def find_knights(cls, name: str) -> Participant:
        for person_name in cls.people:
            if person_name == name:
                return cls.people.get(person_name)

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.people[name] = self
        self.extras = []
        self.weapon = None
        self.armors = {}
        self.protection = 0
        self.plus_effects = None

    @classmethod
    def give_result(cls) -> dict:
        return {
            each_fighter.name: each_fighter.hp
            for each_fighter in cls.fighters
        }

    def apply_armor(self, armor_to_apply: Armor) -> None:
        if self.armors.get(armor_to_apply.part) is not None:
            # stop apply old armor same type
            decrease_hp_armor = self.armors.get(armor_to_apply.part)
            self.protection -= decrease_hp_armor.protection
        # apply new armor
        self.armors.update({armor_to_apply.part: armor_to_apply})
        self.protection += armor_to_apply.protection
        pass

    def apply_weapon(self, weapon_to_apply: Weapon) -> None:
        if self.weapon is not None:
            # stop use current weapon
            self.hp -= self.weapon.power
        # apply new weapon
        self.weapon = weapon_to_apply
        self.power += weapon_to_apply.power
        pass

    def apply_potion(self, potion_to_apply: Potion) -> None:
        if self.plus_effects is not None:
            # stop use current potion
            if self.plus_effects.effect.get("hp") is not None:
                self.hp -= self.plus_effects("hp")
            if self.plus_effects.effect.get("protection") is not None:
                self.protection -= self.plus_effects("protection")
            if self.plus_effects.effect.get("power") is not None:
                self.power -= self.plus_effects("power")
        # apply new potion
        if potion_to_apply.effect.get("hp") is not None:
            self.hp += potion_to_apply.effect.get("hp")
        if potion_to_apply.effect.get("protection") is not None:
            self.protection += potion_to_apply.effect.get("protection")
        if potion_to_apply.effect.get("power") is not None:
            self.power += potion_to_apply.effect.get("power")
        self.plus_effects = potion_to_apply

    def apply_extras(self, extra: Armor | Weapon | Potion) -> None:
        if isinstance(extra, Armor):
            self.apply_armor(extra)
        elif isinstance(extra, Weapon):
            self.apply_weapon(extra)
        else:
            self.apply_potion(extra)
