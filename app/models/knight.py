from .armor import Armour
from .weapon import Weapon
from .status import Status
from .potion import Potion


class Knight:
    def __init__(
        self, name: str, status: Status,
        armour: list[Armor | None],
        weapon: Weapon,
        potion: Potion | None
    ) -> None:
        self.name = name
        self.base_power = status.power
        self.base_hp = status.hp
        self.base_protection = 0
        self.armor = armor
        self.weapon = weapon
        self.potion = potion
        self.refresh_initial_status()
        
    
    def equip_armours(self) -> int:
        return self.base_protection + sum(armour.protection for armour in self.armour)
   
    def equip_weapon(self) -> int:
        return self.base_power + self.weapon.power

    def apply_potion(self):
        for effect, value in self.potion.effect.items():
            self[effect] += value
    
    def refresh_initial_status(self):
        self.protection = self.equip_armours()
        self.power = self.equip_weapon()
        self.apply_potion()
