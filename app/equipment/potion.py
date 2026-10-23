from app.knight import Knight


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply_potion(self, knight: Knight) -> None:
        knight.protection += self.effect.get("protection", 0)
        knight.power += self.effect.get("power", 0)
        knight.hp += self.effect.get("hp", 0)
