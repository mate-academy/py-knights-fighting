from __future__ import annotations


class Knight:
    knights = []

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.protection = 0
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        for element in self.armour:
            self.protection += element["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is None:
            return

        for effect_name, effect_value in self.potion["effect"].items():
            self.__dict__[effect_name] += effect_value

    @classmethod
    def get_knight(cls, name: str) -> Knight:
        for knight in cls.knights:
            if knight.name == name:
                return knight

    @classmethod
    def create_knight(cls, stats: dict) -> Knight:
        knight = Knight(
            stats["name"],
            stats["power"],
            stats["hp"],
            stats["armour"],
            stats["weapon"],
            stats["potion"]
        )
        cls.knights.append(knight)
        return knight
