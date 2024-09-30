from __future__ import annotations

import json

from app.people.person import Person


class Knight(Person):

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list[dict],
                 weapon: dict,
                 potion: dict) -> None:
        super().__init__(name, power, hp)
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    @staticmethod
    def knights_from_dict(knights_dict: dict) -> dict:
        knights = {}
        for knight_name, knight_stats in knights_dict.items():
            knights[knight_name] = Knight.knight_from_dict(knight_stats)
        return knights

    @staticmethod
    def knight_from_dict(knight_stats: dict) -> Knight:
        knight_json = json.dumps(knight_stats)
        return Knight(**json.loads(knight_json))
