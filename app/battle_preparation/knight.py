from __future__ import annotations


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.equipment = None
        self.liquid = None
        self.weapon = None

    def get_ready_for_battle(
            self,
            armor_parts: list,
            miracle_potion: dict,
            divine_weapon: dict
    ) -> None:
        armour = Armour.prepare_armour(armor_parts)
        self.consider_armour_effect(armour)
        potion = Potion.drink_potion(miracle_potion)
        if potion:
            self.consider_potion_effect(potion)
        weapon = Weapon.prepare_weapon(divine_weapon)
        self.consider_weapon(weapon)

    def consider_potion_effect(self, potion: Potion) -> None:
        if "hp" in potion.effect:
            self.hp += potion.effect["hp"]
        if "power" in potion.effect:
            self.power += potion.effect["power"]
        if "protection" in potion.effect:
            self.protection += potion.effect["protection"]
        self.liquid = potion.name

    def consider_armour_effect(self, armour: Armour) -> None:
        self.protection = armour.protection
        self.equipment = armour.equipment

    def consider_weapon(self, weapon: Weapon) -> None:
        self.power += weapon.power
        self.weapon = weapon.name


class Armour:
    def __init__(self, equipment: list, protection: int) -> None:
        self.equipment = equipment
        self.protection = protection

    @classmethod
    def prepare_armour(cls, parts: list) -> Armour:
        protection = 0
        equipment = []
        for part in parts:
            equipment.append(part["part"])
            protection += part["protection"]
        return cls(equipment, protection)


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def prepare_weapon(cls, weapon: dict) -> Weapon:
        return cls(weapon["name"], weapon["power"])


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    @classmethod
    def drink_potion(cls, potion: dict) -> Potion:
        if potion:
            return cls(potion["name"], potion["effect"])
