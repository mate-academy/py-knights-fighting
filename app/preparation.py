from app.knights import Knight


class Preparation:
    def __init__(self, knight: Knight) -> None:
        self.knight = knight

    def preparation_weapon(self) -> None:
        self.knight.power += self.knight.weapon["power"]

    def preparation_armour(self) -> None:
        for armour in self.knight.armour:
            self.knight.protection += armour["protection"]

    def preparation_potion(self) -> None:
        if self.knight.potion is not None:
            for name, boost in self.knight.potion["effect"].items():
                if name == "protection":
                    self.knight.protection += boost
                if name == "power":
                    self.knight.power += boost
                if name == "armour":
                    self.knight.protection += boost
                if name == "hp":
                    self.knight.hp += boost
