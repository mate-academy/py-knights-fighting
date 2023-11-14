from __future__ import annotations

from app.game_objects.game_object import GameObject
from app.game_objects.armour import Armour
from app.game_objects.weapon import Weapon
from app.game_objects.potion import Potion


class Knight(GameObject):
    armour = []
    weapon = None
    potion = None

    def __init__(
            self,
            name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        super().__init__(name)
        self.power = power
        self.hp = hp
        self.protection = protection

    def change_hp(self, delta_hp: int) -> None:
        self.hp += delta_hp
        if self.hp < 0:
            self.hp = 0

    def set_armour(self, armour: Armour) -> None:
        self.armour.append(armour)
        self.protection += armour.protection

    def set_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.power += weapon.power

    def set_potion(self, potion: Potion) -> None:
        self.potion = potion
        self.hp += potion.hp
        self.protection += potion.protection
        self.power += potion.power

    def get_damage(self, enemy: Knight) -> None:
        self.change_hp(self.protection - enemy.power)
