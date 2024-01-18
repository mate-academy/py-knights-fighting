from __future__ import annotations
from app.potion import Potion


class Knight:
    __knights_statistics = {}

    def __new__(cls, knight: dict, *args, **kwargs) -> Knight:
        cls._prepare_for_battle(knight)
        cls.__knights_statistics[knight.get("name")] = knight.get("hp")
        return super().__new__(cls)

    def __init__(self, knight: dict) -> None:
        self.name = knight.get("name")
        self.hp = knight.get("hp")
        self.protection = knight.get("protection") or 0
        self.power = knight.get("power")

    @classmethod
    def _prepare_for_battle(cls, knight_data: dict) -> None:
        if knight_data["armour"]:
            knight_data["protection"] = (
                sum(armor["protection"] for armor in knight_data["armour"])
            )

        knight_data["power"] += knight_data["weapon"]["power"]

        if potion_data := knight_data["potion"]:
            potion = Potion(**potion_data["effect"])
            potion.apply(knight_data)

    @classmethod
    def get_statistics(cls, knights: dict) -> dict:
        for config in knights.values():
            cls.__knights_statistics[config.name] = config.hp
        return cls.__knights_statistics
