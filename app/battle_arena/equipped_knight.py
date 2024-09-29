from __future__ import annotations

from app.people.knight import Knight


class EquippedKnight:

    def __init__(self, knight: Knight) -> None:
        self.name = knight.name
        self.power = knight.power + knight.weapon.get("power")
        self.hp = knight.hp
        self.protection = 0
        if armour := knight.armour:
            self.put_on(armour)
        if potion := knight.potion:
            self.use(potion)

    def put_on(self, armour: list[dict]) -> None:
        for part in armour:
            self.protection += part.get("protection")

    def use(self, potion: dict) -> None:
        effects = potion.get("effect")
        self.power += effects.get("power", 0)
        self.hp += effects.get("hp", 0)
        self.protection += effects.get("protection", 0)
