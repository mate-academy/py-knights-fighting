class Potion:
    """"
    Knight's potion.

    Instead of None default value set to 0
    """

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.hp_boost = effect.get("hp", 0)
        self.power_boost = effect.get("power", 0)
        self.protection_boost = effect.get("protection", 0)

    def to_dict(self) -> dict:
        """"Used to add values from potion in knight's class"""
        return {
            "hp": self.hp_boost,
            "power": self.power_boost,
            "protection": self.protection_boost
        }
