from typing import Union


class Knight:

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: Union[dict, None],
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = (
            sum([i.get("protection", 0) for i in self.armour])
            if self.armour else 0
        )

    def preparation_for_battle(self) -> None:
        if self.weapon:
            self.power += self.weapon["power"]

        if self.potion is not None:
            potion_attr = set(
                self.potion["effect"].keys()) & set(
                self.__dict__.keys()
            )
            for attr in potion_attr:
                self.__dict__[attr] += self.potion["effect"][attr]
