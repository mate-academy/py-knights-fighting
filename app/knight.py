class Knight:
    protection = 0

    def __init__(
        self,
        name: str,
        power: int,
        hp: int,
        armour: list,
        weapon: dict,
        potion: dict
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def set_armour(self) -> None:
        if self.armour:
            for equipment in self.armour:
                self.protection += equipment.get("protection")

    def set_weapon(self) -> None:
        self.power += self.weapon.get("power")

    def set_potion(self) -> None:
        if self.potion:
            if "power" in self.potion.get("effect"):
                self.power += self.potion.get("effect").get("power")
            if "protection" in self.potion.get("effect"):
                self.protection += self.potion.get("effect").get("protection")
            if "hp" in self.potion.get("effect"):
                self.hp += self.potion.get("effect").get("hp")

    def preparation(self) -> None:
        self.set_armour()
        self.set_weapon()
        self.set_potion()
