from app.equipment.armour import Armor
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    UPGRADES = (Armor, Weapon, Potion)

    def __init__(self, **equip) -> None:
        self.name = equip.get("name")
        self.power = equip.get("power")
        self.hp = equip.get("hp")
        self.equipment = equip
        self.protection = 0
        self.weapon = None

    def prepare_for_battle(self) -> None:
        for upgrade_class in Knight.UPGRADES:
            upgrade_class.apply(self)
