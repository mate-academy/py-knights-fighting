class Knight:
    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.hp = knight["hp"]
        self.armor = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.power = knight["power"] + self.weapon["power"]
        self.protection = sum(element.get("protection")
                              for element in self.armor)

    def drink_potion(self, potion: dict) -> None:
        if potion:
            potion = potion["effect"]
            if potion.get("power"):
                self.power += potion.get("power")
            if potion.get("hp"):
                self.hp += potion.get("hp")
            if potion.get("protection"):
                self.protection += potion.get("protection")

    def check_hp(self) -> None:
        if self.hp <= 0:
            print(f"{self.name} fell in battle")
            self.hp = 0
