from app.equipment_module.armour import Armour
from app.equipment_module.potion import Potion
from app.equipment_module.weapon import Weapon


class Knight:

    def __init__(self, knight: dict) -> None:
        self.protection = 0
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]

    def set_knight_armour(self) -> None:
        if self.armour is not None:
            knight_armour = Armour(self.armour)
            for unit in knight_armour.armour_parts:
                self.protection += unit.protection

    def use_potion(self) -> None:
        if self.potion is not None:
            knight_potion = Potion(self.potion)
            self.power += knight_potion.power
            self.hp += knight_potion.hp
            self.protection += knight_potion.protection

    def take_weapon(self) -> None:
        if self.power is not None:
            knight_weapon = Weapon(self.weapon)
            self.power += knight_weapon.power

    def get_ready_to_battle(self) -> None:
        self.use_potion()
        self.take_weapon()
        self.set_knight_armour()
