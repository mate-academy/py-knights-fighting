from __future__ import annotations


class Knight:
    def __init__(self) -> None:
        self.name: str = ''
        self.power: int = 0
        self.hp: int = 0
        self.protection: int = 0

    def _additional_armors(self, armors: list[dict]) -> None:
        for armor in armors:
            self.protection += armor["protection"]

    def _additional_weapon(self, weapon: dict) -> None:
        self.power += weapon["power"]

    def _additional_potion(self, potion: dict) -> None:
        if potion is not None:
            effect = potion["effect"]
            for key, value in effect.items():
                if hasattr(self, key):
                    setattr(self, key, getattr(self, key) + value)

    def initial_all_stats(self, knight: dict) -> Knight:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self._additional_armors(knight["armour"])
        self._additional_weapon(knight["weapon"])
        self._additional_potion(knight["potion"])
        return self
