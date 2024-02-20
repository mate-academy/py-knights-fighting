
class Potion:

    def __init__(self, potion: dict) -> None:
        self.name = potion["name"]
        self.hp = potion["effect"].get("hp", 0)
        self.power = potion["effect"].get("power", 0)
        self.protection = potion["effect"].get("protection", 0)
