from app.items.potion import Potion
from app.items.armour import Armour
from app.items.weapon import Weapon


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = self.apply_armour(armour)
        self.weapon = self.apply_weapon(weapon)
        self.potion = self.apply_potion(potion)

    def apply_armour(self, armour_list: list) -> list:
        res = []
        if armour_list:
            for armour in armour_list:
                res.append(Armour(*armour))
                self.protection += armour["protection"]
        return res

    def apply_weapon(self, weapon: dict) -> list:
        res = Weapon(**weapon)
        self.power += res.power
        return [res]

    def apply_potion(self, potion: dict) -> list:
        res = []
        if potion:
            potion = Potion(potion["name"], **potion["effect"])
            res.append(potion)
            self.protection += potion.protection
            self.power += potion.power
            self.hp += potion.hp
        return res
