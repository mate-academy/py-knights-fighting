class Effect:
    def __init__(self, effect: dict) -> None:
        self.power = effect.get("power", 0)
        self.protection = effect.get("protection", 0)
        self.hp = effect.get("hp", 0)
