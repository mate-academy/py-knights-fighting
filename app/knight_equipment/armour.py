class Armour:
    def __init__(self, armour_list: list) -> None:
        self.armour_list = armour_list

    def equip_armour(self) -> int:
        protection = 0
        for armour in self.armour_list:
            protection += armour["protection"]
        return protection
