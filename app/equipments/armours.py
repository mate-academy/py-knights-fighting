class Armour:
    armours = {}

    def equip_armour(self) -> None:
        for armour in Armour.armours[self.name]:
            self.protection += armour["protection"]
