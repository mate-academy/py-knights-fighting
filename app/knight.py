from __future__ import annotations

from app.gear import Armour, Weapon, Potion


class Knight:
    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.protection = 0
        self.info = knight_info

    @classmethod
    def duel(cls, white_knight: Knight, bleak_knight: Knight) -> None:
        white_knight.hp -= bleak_knight.power - white_knight.protection
        bleak_knight.hp -= white_knight.power - bleak_knight.protection
        white_knight.hp = max(0, white_knight.hp)
        bleak_knight.hp = max(0, bleak_knight.hp)

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
