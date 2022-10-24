class Armour:
    armours = {}

    @staticmethod
    def equip(knight: None) -> None:
        for armr in Armour.armours[knight.name]:
            knight.protection += armr["protection"]
