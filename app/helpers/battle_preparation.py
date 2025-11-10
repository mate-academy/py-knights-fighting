from typing import Any

from app.helpers.apply_armour import Armour
from app.helpers.apply_weapon import Weapon
from app.helpers.potion_usage import UsePotion
from app.knights.knights import Character


class BattlePreparation:
    def __init__(self, name: str, config: dict[Any]) -> None:
        self.name = name
        self.config = config

    def create_character(self) -> Character:
        person = Character(self.name,
                           self.config[self.name]["power"],
                           self.config[self.name]["hp"])

        person.equip_character(self.config)

        person_use_armour = Armour(person)
        person_use_armour.use_armour()

        person_weapon = Weapon(person)
        person_weapon.use_weapon()

        person_use_potion = UsePotion(person)
        person_use_potion.use_all_potion()

        return person
