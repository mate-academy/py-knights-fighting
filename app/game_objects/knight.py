from __future__ import annotations

from app.game_objects.game_object import GameObject
from app.game_objects.armour import Armour
from app.game_objects.weapon import Weapon
from app.game_objects.potion import Potion


class Knight(GameObject):
    armour = []
    weapon = None
    potion = None

    def change_hp(self, delta_hp: int) -> None:
        self.hp += delta_hp
        if self.hp < 0:
            self.hp = 0

    def add_item_properties(self, item: GameObject) -> None:
        self.change_hp(item.hp)
        self.power += item.power
        self.protection += item.protection

    def set_armour(self, armour: Armour) -> None:
        self.armour.append(armour)
        self.add_item_properties(armour)

    def set_weapon(self, weapon: Weapon) -> None:
        self.weapon = weapon
        self.add_item_properties(weapon)

    def set_potion(self, potion: Potion) -> None:
        self.potion = potion
        self.add_item_properties(potion)

    def get_damage(self, enemy: Knight) -> None:
        self.change_hp(self.protection - enemy.power)
