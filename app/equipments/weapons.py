class Weapon:
    weapons = {}

    @staticmethod
    def equip(knight: None) -> None:
        knight.power += Weapon.weapons[knight.name]["power"]
