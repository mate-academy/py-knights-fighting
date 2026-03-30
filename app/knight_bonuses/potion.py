class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.hp = effect.get("hp")
        self.power = effect.get("power")
        self.protection = effect.get("protection")
