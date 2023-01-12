from typing import Union


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[dict],
        weapon: dict,
        potion: Union[None, dict],
    ) -> None:

        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def prepare_to_battle(self) -> None:
        for element in self.armour:
            self.protection += element["protection"]

        self.power += self.weapon["power"]

        if self.potion is not None:
            self.power += self.potion["effect"].get("power", 0)
            self.hp += self.potion["effect"].get("hp", 0)
            self.protection += self.potion["effect"].get("protection", 0)
