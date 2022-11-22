from app.equipment.armour import Armour
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon
from app.keys import KeysKnight


class Knight:

    def __init__(self, dictionary: dict) -> None:
        self.name = dictionary[KeysKnight.NAME.value]
        self.power = dictionary[KeysKnight.POWER.value]
        self.hp = dictionary[KeysKnight.HP.value]
        self.armour = dictionary[KeysKnight.ARMOUR.value]
        self.weapon = dictionary[KeysKnight.WEAPON.value]
        self.potion = dictionary[KeysKnight.POTION.value]
        self.protection = 0

    def apply_weapon(self) -> int:
        weapon = Weapon(self.weapon)
        self.power += weapon.power
        return self.power

    def apply_armour(self) -> int:
        armour = Armour(self.armour)
        self.protection = armour.sum_protect
        return self.protection

    def apply_potion(self) -> tuple:
        if self.potion is not None:
            potion = Potion(self.potion)
            if "power" in potion.effect:
                self.power += potion.effect["power"]

            if "protection" in potion.effect:
                self.protection += potion.effect["protection"]

            if "hp" in potion.effect:
                self.hp += potion.effect["hp"]
        return self.power, self.protection, self.hp

    def prepare_to_battle(self) -> tuple:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self.power, self.protection, self.hp
