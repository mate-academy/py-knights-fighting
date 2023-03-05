from typing import Union


class Knight:
    protection = 0

    def __init__(self, name: str, power: int, hp: int, armour: list,
                 weapon: dict, potion: Union[None | dict]) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def apply_armour(self) -> None:
        for armour_piece in self.armour:
            self.protection += armour_piece["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion_if_exist(self) -> None:
        if self.potion is not None:
            for potion_effect, value in self.potion["effect"].items():
                if potion_effect == "power":
                    self.power += value
                if potion_effect == "protection":
                    self.protection += value
                if potion_effect == "hp":
                    self.hp += value
