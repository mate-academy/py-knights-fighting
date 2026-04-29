from __future__ import annotations


from app.armour import Armour
from app.weapons import Weapon
from app.potion import Potion


class Knight:

    def __init__(self, knight_dict: dict) -> None:

        self.name = knight_dict["name"]

        self.raw_hp = knight_dict["hp"]
        self.raw_power = knight_dict["power"]
        self.raw_protection = 0
        self.armour_protection = 0
        self.potion_name = None
        self.potion_power_effect = 0
        self.potion_hp_effect = 0
        self.potion_protection_effect = 0

# weapon, power
        weapon_obj = Weapon(knight_dict["weapon"])
        self.weapon_power = weapon_obj.power
        self.weapon_name = weapon_obj.name

# armour, protection
        armour_list = knight_dict["armour"]
        armour_list_obj = []
        for armour_part in armour_list:
            armour_part_obj = Armour(armour_part)
            armour_list_obj.append(armour_part_obj)
            self.armour_protection += armour_part_obj.protection

# potion, potion stats
        potion_obj = Potion(knight_dict["potion"])
        if potion_obj.name is not None:
            self.potion_name = potion_obj.name
            self.potion_power_effect = potion_obj.power_effect
            self.potion_hp_effect = potion_obj.hp_effect
            self.potion_protection_effect = potion_obj.protection_effect

# final stats
        self.power = (self.raw_power + self.weapon_power
                      + self.potion_power_effect)
        self.hp = self.raw_hp + self.potion_hp_effect
        self.protection = (self.raw_protection + self.armour_protection
                           + self.potion_protection_effect)
        self.max_hp = self.hp

    def take_damage(self, opponent: Knight) -> None:
        damage = opponent.power - self.protection
        if damage < 0:
            damage = 0
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self) -> None:
        self.hp = self.max_hp
        print(f"{self.name} has been healed!")
