from __future__ import annotations
from abc import ABC


class Player(ABC):
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            inventory: dict,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.inventory = inventory
        self.protection = protection

    @classmethod
    def create_from_dict(cls, player: dict) -> Player:
        from app.items.equipment.weapon import Weapon
        from app.items.equipment.armour import Armour
        from app.items.potion import Potion

        name = player["name"]
        power = player["power"]
        hp = player["hp"]
        weapon = Weapon.create_from_dict(player["weapon"])
        potion = Potion.create_from_dict(player["potion"])
        armours = dict()
        for armour in player["armour"]:
            armours[armour["part"]] = Armour.create_from_dict(armour)
        inventory = {"weapon": weapon, "potion": potion, "armour": armours}
        return cls(name, power, hp, inventory)

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = max(0, value)

    def equip_weapon(self) -> None:
        weapon = self.inventory["weapon"]
        if weapon:
            weapon.use(self)

    def unequip_weapon(self) -> None:
        weapon = self.inventory["weapon"]
        if weapon:
            weapon.unuse(self)

    def drink_potion(self) -> None:
        potion = self.inventory["potion"]
        self.inventory["potion"] = None
        if potion:
            potion.use(self)

    def equip_armour(self, armour_part_name: str) -> None:
        armour = self.inventory["armour"][armour_part_name]
        if armour:
            armour.use(self)

    def unequip_armour(self, armour_part_name: str) -> None:
        armour = self.inventory["armour"][armour_part_name]
        if armour:
            armour.unuse(self)

    def equip_armour_all(self) -> None:
        for armour_part_name in self.inventory["armour"]:
            self.equip_armour(armour_part_name)

    def unequip_armour_all(self) -> None:
        for armour_part_name in self.inventory["armour"]:
            self.unequip_armour(armour_part_name)

    def prepare_for_battle(self) -> None:
        self.equip_weapon()
        self.equip_armour_all()
        self.drink_potion()

    def add_item_to_inventory(self) -> None:
        pass

    def romove_item_form_inventory(self) -> None:
        pass
