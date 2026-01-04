from __future__ import annotations


class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: Armour | None,
                 weapon: Weapon,
                 potion: Potion | None
                 ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def __str__(self) -> str:
        if self.armour is not None:
            helmet = self.armour.helmet
            breastplate = self.armour.breastplate
            boots = self.armour.boots

        armour = "no armour"
        if self.armour is not None:
            armour = f"helmet: {helmet} chest: {breastplate} boots: {boots}"

        potion = "no potion"
        if self.potion is not None:
            potion = f"{self.potion.name} -> \
pwr: {self.potion.power} hp: {self.potion.hp} prot: {self.potion.protection}"

        return f"Name: {self.name}, power: {self.power}, health: {self.hp}\n\
Armou -> {armour}\n\
Weapon: {self.weapon.name} -> power: {self.weapon.power}\n\
Potion: {potion}"

    @classmethod
    def recruit_a_knight(cls, knight: dict) -> Knight:

        name = knight["name"]
        power = knight["power"]
        health = knight["hp"]
        armour = None
        weapon = Weapon.add_weapon(knight["weapon"])
        potion = None

        if knight["armour"]:
            armour = Armour.add_armour(knight["armour"])

        if knight["potion"]:
            potion = Potion.add_potion(knight["potion"])

        return Knight(name, power, health, armour, weapon, potion)


class EquippedKnight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def equip_knight(cls, knight: Knight) -> EquippedKnight:
        power = knight.power + knight.weapon.power
        hp = knight.hp
        protection = 0
        if knight.armour is not None:
            protection += Armour.sum_armour(knight.armour)
        if knight.potion is not None:
            power += knight.potion.power
            hp += knight.potion.hp
            protection += knight.potion.protection
        return EquippedKnight(knight.name, power, hp, protection)


class Armour:
    def __init__(self, helmet: int, breastplate: int, boots: int) -> None:
        self.helmet = helmet
        self.breastplate = breastplate
        self.boots = boots

    @classmethod
    def add_armour(cls, armour: list) -> Armour:
        helmet, breastplate, boots = 0, 0, 0
        for part in armour:
            if part["part"] == "helmet":
                helmet += part["protection"]
            if part["part"] == "breastplate":
                breastplate += part["protection"]
            if part["part"] == "boots":
                boots += part["protection"]
        return Armour(helmet, breastplate, boots)

    @classmethod
    def sum_armour(cls, armour: Armour) -> int:
        return armour.helmet + armour.breastplate + armour.boots


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def add_weapon(cls, weapon: dict) -> Weapon:
        return Weapon(weapon["name"], weapon["power"])


class Potion:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def add_potion(cls, potion: dict) -> Potion:
        name = potion["name"]
        effect = potion["effect"]
        power = effect.get("power", 0)
        hp = effect.get("hp", 0)
        protection = effect.get("protection", 0)
        return Potion(name, power, hp, protection)
