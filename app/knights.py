class Knights:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def apply_armour(self) -> None:
        for element in self.armour:
            self.protection += element["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion:
            if self.potion.get("effect").get("power"):
                self.power += self.potion.get("effect").get("power")

            if self.potion.get("effect").get("protection"):
                self.protection += self.potion.get("effect").get("protection")

            if self.potion.get("effect").get("hp"):
                self.hp += self.potion.get("effect").get("hp")
