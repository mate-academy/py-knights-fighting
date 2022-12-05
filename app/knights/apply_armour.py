from app.knights.apply_weapon import Weapon


class Armour:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_armour(self) -> dict:
        for hero in self.knight:
            self.knight[hero]["protection"] = 0
            for a in self.knight[hero]["armour"]:
                self.knight[hero]["protection"] += a["protection"]

        return Weapon(self.knight).apply_weapon()
