from app.config.knights import Knight

class RedKnight(Knight) :
    def __init__(self, name: str, weapon: dict, power: int, hp: int, armour: list, potion: dict = None) -> None:
        super().__init__(name, weapon, power, hp, armour, potion)
