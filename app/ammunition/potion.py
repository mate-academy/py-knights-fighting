class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.hp_boost = effect.get("hp")
        self.power_boost = effect.get("power")
        self.protection_boost = effect.get("protection")
        if self.hp_boost is None:
            self.hp_boost = 0
        if self.power_boost is None:
            self.power_boost = 0
        if self.protection_boost is None:
            self.protection_boost = 0

    def to_dict(self) -> dict:
        return {
            "hp": self.hp_boost,
            "power": self.power_boost,
            "protection": self.protection_boost
        }
