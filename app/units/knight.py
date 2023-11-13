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
            for item in potion.effect:
                match item:
                    case KeysKnight.POWER.value:
                        self.power += potion.effect[
                            KeysKnight.POWER.value]
                    case KeysKnight.PROTECTION.value:
                        self.protection += potion.effect[
                            KeysKnight.PROTECTION.value]
                    case KeysKnight.HP.value:
                        self.hp += potion.effect[
                            KeysKnight.HP.value]
        return self.power, self.protection, self.hp

    def prepare_to_battle(self) -> __build_class__:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
        return self
