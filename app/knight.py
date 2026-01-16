from __future__ import annotations

from app.gear import Armour, Weapon, Potion


class Knight:
    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.protection = 0
        self.info = knight_info

    def duel(self, other_knight: Knight) -> None:
        self.hp -= other_knight.power - self.protection
        other_knight.hp -= self.power - other_knight.protection
        self.hp = max(0, self.hp)
        other_knight.hp = max(0, other_knight.hp)

    def apply_gear(self) -> None:
        self.put_armor()
        self.take_weapon()
        self.drink_potion()

    def put_armor(self) -> None:
        armours = []
        for subject_info in self.info["armour"]:
            armour = Armour(subject_info)
            armours.append(armour)
            self.protection += armour.protection
        self.armour = armours

    def take_weapon(self) -> None:
        self.weapon = Weapon(self.info["weapon"])
        self.power += self.weapon.power

    def drink_potion(self) -> None:
        if self.info["potion"] is None:
            return

        self.potion = Potion(self.info["potion"])

        for effect, value in self.potion.effect.items():
            setattr(self, effect, value + getattr(self, effect))
