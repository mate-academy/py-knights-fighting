from app.equipment.armour import Armour
from app.equipment.weapon import Weapon
from app.equipment.potion import Potion


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.name = knight_data["name"]
        self.power = knight_data["power"]
        self.hp = knight_data["hp"]
        self.armour = [Armour(armour) for armour in knight_data["armour"]]
        self.weapon = Weapon(knight_data["weapon"])
        self.potion = Potion(knight_data["potion"])
        self.protection = 0

    def apply_armour(self) -> None:
        self.protection += Armour.get_total_protection(self.armour)

    def apply_weapon(self) -> None:
        self.power += self.weapon.power

    def apply_potion(self) -> (int, int, int):
        self.hp += self.potion.hp_effect
        self.power += self.potion.power_effect
        self.protection += self.potion.protection_effect

    def prepare_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()
