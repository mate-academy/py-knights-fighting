from object.armour import Armour
from object.potion import Potion
from object.weapon import Weapon


class Knight:
    def __init__(self,
                 name: str,
                 hp: int,
                 power: int,
                 armour: list[Armour],
                 potion: Potion | None,
                 weapon: Weapon) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.armour = armour
        self.potion = potion
        self.weapon = weapon
        self.protection = 0

    def __repr__(self) -> str:
        return f"""
\n<
    Knight Name: {self.name}
    Knight HP: {self.hp}
    Knight Protection: {self.protection}
    Knight Power: {self.power}
    Knight Armour: {self.armour}
    Knight Potion: {self.potion}
    Knight Weapon: {self.weapon}
>
"""
