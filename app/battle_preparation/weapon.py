from app.battle_preparation.knight import Knight


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def prepare_weapon(cls, weapon: dict) -> "Weapon":
        return cls(weapon["name"], weapon["power"])

    def consider_weapon(self, knight: Knight) -> None:
        knight.power += self.power
        knight.weapon = self.name
