from __future__ import annotations

from app.people.knight import Knight


class EquippedKnight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def put_on(self, armour: list[dict]) -> None:
        for part in armour:
            self.protection += part.get("protection")

    def use(self, potion: dict) -> None:
        effects = potion.get("effect")
        self.power += effects.get("power", 0)
        self.hp += effects.get("hp", 0)
        self.protection += effects.get("protection", 0)

    @staticmethod
    def equipped_knight_from_knight(knight: Knight) -> EquippedKnight:
        name = knight.name
        power = knight.power + knight.weapon.get("power")
        hp = knight.hp
        protection = 0
        equipped_knight = EquippedKnight(name, power, hp, protection)
        if armour := knight.armour:
            equipped_knight.put_on(armour)
        if potion := knight.potion:
            equipped_knight.use(potion)
        return equipped_knight

    @staticmethod
    def equipped_knights_from_knights(knights: dict) -> dict:
        equipped_knights_dict = {}
        for knight_name, knight in knights.items():
            equipped_knights_dict[knight_name]\
                = EquippedKnight.equipped_knight_from_knight(knight)
        return equipped_knights_dict
