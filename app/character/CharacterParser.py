from __future__ import annotations

from app.character.Character import Character
from app.character.Inventory import Inventory
from app.item.consumables.Potion import Potion
from app.item.wearable.Armour import Armour
from app.item.wearable.Weapon import Weapon


class CharacterParser:
    @staticmethod
    def parse(characters_dict: dict) -> list[Character]:

        characters = []

        for chr_data in characters_dict.values():
            character_name = chr_data["name"]
            character_power = chr_data["power"]
            character_hp = chr_data["hp"]

            character_item_list = []

            for character_armour in chr_data["armour"]:
                character_item_list.append(
                    Armour(character_armour["part"],
                           character_armour["protection"])
                )

            character_item_list.append(
                Weapon(chr_data["weapon"]["name"],
                       chr_data["weapon"]["power"])
            )

            if chr_data["potion"]:
                character_item_list.append(
                    Potion(chr_data["potion"]["name"],
                           chr_data["potion"]["effect"].get("hp", 0),
                           chr_data["potion"]["effect"].get("power", 0),
                           chr_data["potion"]["effect"].get("protection", 0))
                )

            character_inventory = Inventory(character_item_list)
            characters.append(
                Character(character_name,
                          character_power,
                          character_hp,
                          character_inventory
                          )
            )

        return characters
