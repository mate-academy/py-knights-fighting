from app.equipment.armor import Armor
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    UPGRADES = (Armor, Weapon, Potion)

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        self.equip_list = None
        self.weapon = None
        self.config = None

    def prepare_for_battle(self, config: dict) -> None:
        self.config = config
        for upgrade_class in Knight.UPGRADES:
            upgrade_class.apply(self, self.config)
