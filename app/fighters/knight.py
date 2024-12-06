from __future__ import annotations

from array import array
from email.encoders import encode_quopri

from app.adapters.knight_config import KnightConfig
from app.item_system.items import Item, Weapon, Potion, Armour
from app.item_system.inventory import Inventory
from app.utils.formatting import number_as_bar, list_to_string


class Knight:
    def __init__(self, knight_data: KnightConfig) -> None:
        self._name = knight_data.name
        self._power = knight_data.power
        self._hp = knight_data.hp
        self._protection = knight_data.protection
        self._inventory = Inventory(knight_data.inventory_data)

        self._equiped_armour = []
        self._equiped_weapon = None
        self._applied_potion = None

    def __str__(self) -> str:
        equiped_armour_str = "absolutely nothing"
        if self.equiped_armour:
            equiped_armour_str = list_to_string(self.equiped_armour)

        equiped_weapons_str = "nothing"
        if self.equiped_weapon:
            equiped_weapons_str = self.equiped_weapon

        return (
            f"Sir {self.name}\n"
            f"        HEALTH\n"
            f"({number_as_bar(self.hp)})\n"
            f"Armed with {equiped_weapons_str}\n"
            f"Wearing {equiped_armour_str}\n"
            f"(protection: {self.protection})\n"
            f"{str(self.inventory)}"
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, value: int) -> None:
        if value >= 0:
            self._power = value
        else:
            self._power = 0

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        if value >= 0:
            self._hp = value
        else:
            self._hp = 0

    @property
    def protection(self) -> int:
        return self._protection

    @protection.setter
    def protection(self, value: int) -> None:
        self._protection = value

    @property
    def inventory(self):
        return self._inventory

    @property
    def equiped_weapon(self) -> Weapon:
        return self._equiped_weapon

    @equiped_weapon.setter
    def equiped_weapon(self, weapon: Weapon) -> None:
        print(f"{self.name} equips {weapon}")
        self._equiped_weapon = weapon

    @property
    def equiped_armour(self):
        return self._equiped_armour

    @property
    def applied_potion(self):
        return self._applied_potion

    @applied_potion.setter
    def applied_potion(self, potion: Potion) -> None:
        self._applied_potion = potion

    def equip_best_weapon(self) -> None:
        if self.inventory.get_weapons():
            best_weapon = max(self.inventory.get_weapons())

            if not self.equiped_weapon:
                self.equiped_weapon = best_weapon
                self.inventory.remove(best_weapon)
                self.apply_item_effect(best_weapon)
            else:
                print(f"{self.name} already has {self.equiped_weapon.name}")

    def unequip_weapon(self) -> None:
        if self.equiped_weapon:
            self.revert_item_effect(self.equiped_weapon)
            self.inventory.add(self.equiped_weapon)
            self.equiped_weapon = None
        else:
            print("No weapon to uneqip")

    def drink_best_potion(self):
        if self.inventory.get_potions():
            best_potion = max(self.inventory.get_potions())

            if not self.applied_potion:
                print(f"{self.name} drinks {best_potion.name}")
                self.applied_potion = best_potion
                self.inventory.remove(best_potion)
                self.apply_item_effect(best_potion)
            else:
                print(f"{self.name} is drunk enough")

    def equip_all_armour(self):
        armour = tuple(self.inventory.get_armour())
        for armour_piece in armour:
            print(f"{self.name} puts on {armour_piece.name}")
            self.equiped_armour.append(armour_piece)
            self.apply_item_effect(armour_piece)
            self.inventory.remove(armour_piece)

    def apply_item_effect(self, item: Item):
        print(f"{self.name} now has effect of {item}")
        self.hp += item.effect.hp
        self.power += item.effect.power
        self.protection += item.effect.protection

    def revert_item_effect(self, item: Item):
        print(f"{self.name} no longer has effect of {item}")
        self.hp -= item.effect.hp
        self.power -= item.effect.power
        self.protection -= item.effect.protection

    def get_hit(self, power: int) -> None:
        ...

    def attack(self, other: Knight) -> None:
        ...

    def is_alive(self) -> bool:
        if self.hp <= 0:
            return False
        return True
