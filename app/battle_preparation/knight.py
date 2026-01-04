from __future__ import annotations


class Knight:
    KNIGHTS = []

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.equipment = None
        self.liquid = None
        self.weapon = None
        Knight.KNIGHTS.append({self.name: self})

    def get_ready_for_battle(
            self,
            armor_parts: list,
            miracle_potion: dict,
            divine_weapon: dict
    ) -> None:
        self.prepare_armor(armor_parts)
        if miracle_potion:
            self.drink_potion(miracle_potion)
        self.prepare_weapon(divine_weapon)
        self.consider_effects()

    def drink_potion(self, miracle_potion: dict) -> None:
        self.liquid = Potion(miracle_potion["name"], miracle_potion["effect"])

    def consider_potion_effect(self) -> None:
        if not self.liquid:
            return
        self.hp += self.liquid.effect.get("hp", 0)
        self.power += self.liquid.effect.get("power", 0)
        self.protection += self.liquid.effect.get("protection", 0)

    def prepare_armor(self, armor_parts: list) -> None:
        protection = 0
        equipment = []
        for part in armor_parts:
            equipment.append(part["part"])
            protection += part["protection"]
        self.equipment = Armour(equipment, protection)

    def consider_effects(self) -> None:
        self.consider_armor_effect()
        self.consider_potion_effect()
        self.consider_sword_effect()

    def consider_armor_effect(self) -> None:
        self.protection = self.equipment.protection

    def prepare_weapon(self, divine_weapon: dict) -> None:
        self.weapon = Weapon(divine_weapon["name"], divine_weapon["power"])

    def consider_sword_effect(self) -> None:
        self.power += self.weapon.power

    def print_info(self) -> None:
        print(
            f"Name: {self.name}\n"
            f"Power: {self.power}, HP: {self.hp}, "
            f"Protection: {self.protection}"
        )

    def __repr__(self) -> str:
        return (
            f"Name: {self.name} "
            f"Power: {self.power}, HP: {self.hp}, "
            f"Protection: {self.protection}\n"
        )


class Armour:
    def __init__(self, equipment: list, protection: int) -> None:
        self.equipment = equipment
        self.protection = protection

    def __str__(self) -> str:
        return f"Equipment: {self.equipment}\nProtection: {self.protection}"


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f"Name: {self.name}\nPower: {self.power}"


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def __str__(self) -> str:
        return f"Name: {self.name}\nEffect: {self.effect}"
