class Knight:
    def __init__(self, equipment: dict) -> None:
        self.name = equipment.get("name")
        self.hp = equipment.get("hp")
        self.power = equipment.get("power")
        self.protection = 0
        self.armour = equipment.get("armour")
        self.weapon = equipment.get("weapon")
        self.potion = equipment.get("potion")

    def apply_potion(self) -> None:
        for stat, value in self.potion.get("effect").items():
            if stat == "hp":
                self.hp += value
            if stat == "power":
                self.power += value
            if stat == "protection":
                self.protection += value

    def apply_armour(self) -> None:
        for armour_part in self.armour:
            self.protection += armour_part.get("protection")

    def apply_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def apply_all(self) -> None:
        if self.armour:
            self.apply_armour()
        if self.weapon:
            self.apply_weapon()
        if self.potion:
            self.apply_potion()
