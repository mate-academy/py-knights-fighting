from app.knights import Knight


class Preparation:
    def __init__(self, knight: Knight) -> None:
        self.knight = knight

    def full_preparation(self) -> None:
        self.knight.power += self.knight.weapon["power"]

        for armour in self.knight.armour:
            self.knight.protection += armour["protection"]

        if self.knight.potion is not None:
            for name, boost in self.knight.potion["effect"].items():
                setattr(
                    self.knight, name,
                    getattr(self.knight, name)
                    + boost
                )
