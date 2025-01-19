from equipment.weapons import Weapon
from equipment.armour import Armour
from equipment.potions import Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list[Armour],
        weapon: Weapon,
        potion: Potion = None
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0
        self.apply_armour()

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.protection = sum(a.protection for a in self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> None:
        if not self.potion:
            return
        self.power += self.potion.effect.get("power", 0)
        self.hp += self.potion.effect.get("hp", 0)
        self.protection += self.potion.effect.get("protection", 0)
