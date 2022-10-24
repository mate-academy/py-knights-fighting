class Weapon:
    weapons = {}

    def equip_weapon(self) -> None:
        self.power += Weapon.weapons[self.name]["power"]
