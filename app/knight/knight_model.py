from __future__ import annotations


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int = 0
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def armour(self, armour: list) -> int:
        for part in armour:
            self.protection += part["protection"]
        return self.hp

    def weapon(self, weapon_power: int) -> int:
        self.power += weapon_power
        return self.power

    @staticmethod
    def get_item(value_of_dict: dict, item: str) -> int:
        return value_of_dict[item] if value_of_dict.get(item) else 0

    def apply_potion(self, potion: dict | None) -> None:
        if potion is not None:
            self.hp += Knight.get_item(potion["effect"], "hp")
            self.power += Knight.get_item(potion["effect"], "power")
            self.protection += Knight.get_item(potion["effect"], "protection")
