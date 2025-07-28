from app.grounds.equipment_racks import Armour, Weapon, Potion


class Knight:
    def __init__(
        self,
        name: str,
        power: str,
        hp: str,
        equip_list: list
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.equip_list = equip_list
        self.protection = 0
        self.equipment_applied = False

    def apply_equip(self) -> None:
        for equip in self.equip_list:
            if isinstance(equip, Weapon):
                self.power += equip.power
            elif isinstance(equip, Armour):
                self.protection += equip.protection
            elif isinstance(equip, Potion):
                self.power += equip.power_effect
                self.protection += equip.protection_effect
                self.hp += equip.hp_effect
        self.equipment_applied = True
