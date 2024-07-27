from app.equipment.armor import Armor
from app.equipment.potion import Potion
from app.equipment.weapon import Weapon


class Knight:
    def __init__(self, name: str, power: int, hp: int, armor: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armor = armor
        self.equip_list = None
        self.weapon = None
        self.config = None

    def prepare_for_battle(self, config: dict) -> None:
        self.config = config
        for cl in (Armor, Weapon, Potion):
            cl.apply(self, self.config)
