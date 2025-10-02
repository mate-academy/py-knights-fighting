from __future__ import annotations

from copy import deepcopy
from typing import Optional


class PrepareKnight:
    def __init__(self, knights_dict: dict) -> None:
        self.knights_dict = deepcopy(knights_dict)
        self.prepare_knight_for_battle(self.knights_dict)

    def get_all_prepared_knight(self) -> dict:
        knight_names = self.knights_dict.keys()

        return {
            name: self.get_prepared_knight(name)
            for name in knight_names
        }

    def get_prepared_knight(self, knight_name: str) -> dict:
        return self.knights_dict[knight_name]

    def prepare_knight_for_battle(self, knights_dict: dict) -> dict:
        for _, knight in knights_dict.items():
            knight["protection"] = 0
            self.wear_armor(knight)
            knight["power"] += knight["weapon"]["power"]
            self.apply_potions(knight_potion=knight["potion"], knight=knight)
        return self.knights_dict

    @staticmethod
    def wear_armor(knight: dict) -> None:
        for armour in knight["armour"]:
            knight["protection"] += armour["protection"]

    @staticmethod
    def apply_potions(
            knight_potion: Optional[dict | None],
            knight: dict
    ) -> None:
        if knight_potion is not None:
            if "power" in knight_potion["effect"]:
                knight["power"] += knight_potion["effect"]["power"]

            if "protection" in knight_potion["effect"]:
                knight["protection"] += knight_potion["effect"]["protection"]

            if "hp" in knight_potion["effect"]:
                knight["hp"] += knight_potion["effect"]["hp"]
