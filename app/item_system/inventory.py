from typing import Type

from app.adapters.inventory_config import InventoryConfig
from app.item_system.items import Item, Weapon, Armour, Potion
from app.utils.formatting import list_to_string


class Inventory:
    def __init__(self, inventory_data: InventoryConfig):
        self._items_by_category = {
            Weapon: list(
                Weapon.make_items(inventory_data.weapon_datas)
            ),

            Armour: list(
                Armour.make_items(inventory_data.armour_datas)
            ),

            Potion: list(
                Potion.make_items(inventory_data.potion_datas)
            ),
        }

    def __str__(self) -> str:
        item_strings = []

        weapons = self.items_by_category.get(Weapon)
        armour = self.items_by_category.get(Armour)
        potions = self.items_by_category.get(Potion)

        if weapons:
            item_strings.append(f"    Weapons: {list_to_string(weapons)}")
        if armour:
            item_strings.append(f"    Armour: {list_to_string(armour)}")
        if potions:
            item_strings.append(f"    Potions: {list_to_string(potions)}")

        if item_strings:
            return (
                f"Inventory: [\n"
                f"{'\n'.join(item_strings)}\n"
                f"]"
            )

        return "Inventory empty"

    @property
    def items_by_category(self):
        return self._items_by_category

    def add(self, item: Item) -> None:
        for category, items in self.items_by_category.items():
            if isinstance(item, category):
                items.append(item)

    def remove(self, item: Item):
        for items in self.items_by_category.values():
            if item in items:
                items.remove(item)

    def get(self, item: Item) -> Item:
        for items in self.items_by_category.values():
            if item in items:
                return item
    
    def get_weapons(self) -> list[Weapon]:
        return self.items_by_category[Weapon]
    
    def get_armour(self) -> list[Armour]:
        return self.items_by_category[Armour]
    
    def get_potions(self) -> list[Potion]:
        return self.items_by_category[Potion]
