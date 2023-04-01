from typing import Any


class Knights:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armor: list[dict | None],
                 weapon: dict,
                 potion: Any,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def add_equipment(self) -> None:
        # add ammunition
        for ammunition in self.armor:
            self.protection += ammunition["protection"]

        # add weapon
        self.power += self.weapon["power"]

        # add potion
        if self.potion is not None:
            for effect, value in self.potion["effect"].items():
                setattr(self, effect, getattr(self, effect) + value)
