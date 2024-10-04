class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

        self.hp = self.effect.get("hp", 0)
        self.power = self.effect.get("power", 0)
        self.protection = self.effect.get("protection", 0)
