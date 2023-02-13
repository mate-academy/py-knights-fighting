from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    knights_arr = {}

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour_list: list[Armour],
            weapon: Weapon,
            potion: Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour_list = armour_list
        self.weapon = weapon
        self.potion = potion
        self.protection = 0

        if self.name not in Knight.knights_arr:
            Knight.knights_arr[self.name] = self

    def get_ready_for_fight(self) -> None:
        for armour in self.armour_list:
            self.protection += armour.protection

        if self.potion:
            self.hp += self.potion.hp
            self.power += self.potion.power
            self.protection += self.potion.protection

        self.power += self.weapon.power
