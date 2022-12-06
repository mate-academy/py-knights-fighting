from app.knights.apply_potion import Potion


class Weapon:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_weapon(self) -> dict:
        for hero in self.knight:
            self.knight[hero]["power"] += self.knight[hero]["weapon"]["power"]
        return Potion(self.knight).apply_potion()
