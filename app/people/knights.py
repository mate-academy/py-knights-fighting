from app.grounds.equipment_racks import Armour, Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        weapon: Weapon,
        equip_list: list
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.weapon = weapon
        self.equip_list = equip_list
        self.protection = 0
        self.equipment_applied = False

    def apply_equip(self) -> None:
        self.power += self.weapon.power
        for equip in self.equip_list:
            if isinstance(equip, Armour):
                self.protection += equip.protection
            elif isinstance(equip, Potion):
                self.power += equip.power_effect
                self.protection += equip.protection_effect
                self.hp += equip.hp_effect
        self.equipment_applied = True
