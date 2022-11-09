from __future__ import annotations
from app.equipment.Armour import Armour
from app.equipment.Weapon import Weapon
from app.equipment.Potion import Potion


class Knight:
    """Creates a new knight"""
    def __init__(self, character: dict) -> None:
        self.name = character["name"]
        self.power = character["power"]
        self.hp = character["hp"]
        self.armour = Armour(character["armour"])
        self.weapon = Weapon(character["weapon"])
        self.potion = Potion(character["potion"]) \
            if character["potion"] else None
        self.protection = 0

    def ready_for_war(self) -> None:
        """applying all available equipment"""
        if self.weapon:
            Weapon.apply_weapon(self.weapon, self)
        if self.armour:
            Armour.apply_armour(self.armour, self)
        if self.potion:
            Potion.apply_potion(self.potion, self)

    def fight(self, knight2: Knight) -> None:
        self.hp -= knight2.power - self.protection
        knight2.hp -= self.power - knight2.protection

        # check if someone fell in battle
        if self.hp <= 0:
            self.hp = 0

        if knight2.hp <= 0:
            knight2.hp = 0
