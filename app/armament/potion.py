class Potion:
    def __init__(self, name: str, effect: dict[str, int]) -> None:
        self.name = name
        self.hp = effect.get("hp", 0)
        self.power = effect.get("power", 0)
        self.armour = effect.get("protection", 0)
