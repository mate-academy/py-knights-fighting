class Potion:
    def __init__(self, name: str, effect_dict: dict) -> None:
        self.name: str = name
        self.hp_effect: int = effect_dict.get("hp", 0)
        self.power_effect: int = effect_dict.get("power", 0)
        self.protection_effect: int = effect_dict.get("protection", 0)

    def __repr__(self) -> str:
        return (
            f"Potion(name='{self.name}', hp_effect={self.hp_effect}, "
            f"power_effect={self.power_effect}, "
            f"protection_effect={self.protection_effect})"
        )
