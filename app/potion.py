from __future__ import annotations


class Potion:
    def __new__(cls, *args, **kwargs) -> Potion:
        return super().__new__(cls)

    def __init__(
            self,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        self.power = power
        self.hp = hp
        self.protection = protection

    def apply(self, knight_data: dict) -> dict:
        for stat, boost in self._get_attributes().items():
            knight_data[stat] = knight_data.get(stat, 0) + boost
        return knight_data

    def _get_attributes(self) -> dict:
        return {
            "hp": self.hp,
            "power": self.power,
            "protection": self.protection
        }
