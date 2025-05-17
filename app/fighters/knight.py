from __future__ import annotations

from adapters.knight_config import KnightConfig
from item_system.items import Item
from item_system.inventory import Inventory
from utils.formatting import number_as_bar, list_to_string


class Knight:
    """
    Represents a knight

    Properties:
        name (str): knight's name
        power (int): knight's attack power
        hp (str): knight's Health Points
        protection (int): knight's protection
        inventory (Inventory):
            knight's Inventory object, stores not equipped items
        equipped_armour (list[Armour]):
            Armour items that have been equipped
        equipped_weapon (Weapon): weapon that has been equipped
        applied_potion (Potion): potion that has been applied

    Methods:
        equip_best_weapon:
            get the best weapon from Inventory and equip it
        unequip_weapon:
            remove weapon from equipped_weapon and add it to the Inventory
        drink_best_potion:
            get the best potion from inventory and apply it
        equip_all_armour:
            add all armour from the inventory to the equiped_armour list
            and apply it
        apply_item_effect:
            add stats from Effect to knight's stats
        attack:
            pass knight's power to other knight's get_hit method
        get_hit:
            subtract protection from power to calculate damage
            then subtract damage from knight's hp
        is_alive:
            True if hp > 0, False otherwise
        health_as_hp_bar:
            get string with knight's name and hp as bar of '[+]'
    """

    def __init__(self, knight_data: KnightConfig) -> None:
        self._name = knight_data.name
        self._power = knight_data.power
        self._hp = knight_data.hp
        self._protection = knight_data.protection
        self._inventory = Inventory(knight_data.inventory_data)

        self._equipped_armour: list[Item] = []
        self._equipped_weapon: Item | None = None
        self._applied_potion: Item | None = None

    def __str__(self) -> str:
        equipped_armour_str = "absolutely nothing"
        if self.equipped_armour:
            equipped_armour_str = list_to_string(self.equipped_armour)

        equipped_weapons_str = "nothing"
        if self.equipped_weapon:
            equipped_weapons_str = str(self.equipped_weapon)

        return (
            f"Sir {self.name}\n"
            f"{self.health_as_bar()}\n"
            f"Armed with {equipped_weapons_str}\n"
            f"Wearing {equipped_armour_str}\n"
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
    def inventory(self) -> Inventory:
        return self._inventory

    @property
    def equipped_weapon(self) -> Item | None:
        return self._equipped_weapon

    @equipped_weapon.setter
    def equipped_weapon(self, weapon: Item) -> None:
        self._equipped_weapon = weapon

    @property
    def equipped_armour(self) -> list[Item]:
        return self._equipped_armour

    @property
    def applied_potion(self) -> Item | None:
        return self._applied_potion

    @applied_potion.setter
    def applied_potion(self, potion: Item) -> None:
        self._applied_potion = potion

    def equip_best_weapon(self) -> None:
        if self.inventory.get_weapons():
            best_weapon = max(self.inventory.get_weapons())

            if not self.equipped_weapon:
                self.equipped_weapon = best_weapon
                self.inventory.remove(best_weapon)
                self.apply_item_effect(best_weapon)

    def drink_best_potion(self) -> None:
        if self.inventory.get_potions():
            best_potion = max(self.inventory.get_potions())

            if not self.applied_potion:
                self.applied_potion = best_potion
                self.inventory.remove(best_potion)
                self.apply_item_effect(best_potion)

    def equip_all_armour(self) -> None:
        armour = tuple(self.inventory.get_armour())

        for armour_piece in armour:
            self.equipped_armour.append(armour_piece)
            self.apply_item_effect(armour_piece)
            self.inventory.remove(armour_piece)

    def apply_item_effect(self, item: Item) -> None:
        self.hp += item.effect.hp
        self.power += item.effect.power
        self.protection += item.effect.protection

    def get_hit(self, attack_power: int) -> None:
        damage = attack_power - self.protection
        self.hp -= damage

    def attack(self, other: Knight) -> None:
        if other.equipped_weapon is not None:
            other.get_hit(self.power)
        else:
            raise Exception("Cannot attack unarmed target")

    def is_alive(self) -> bool:
        if self.hp <= 0:
            return False
        return True

    def health_as_bar(self) -> str:
        return f"{self.name}: \n" f"            HEALTH\n" f"{number_as_bar(self.hp)}"
