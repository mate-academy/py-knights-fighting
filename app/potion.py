class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def get_power(self) -> int:
        return self.effect.get("power", 0)

    def get_protection(self) -> int:
        return self.effect.get("protection", 0)

    def get_hp(self) -> int:
        return self.effect.get("hp", 0)
