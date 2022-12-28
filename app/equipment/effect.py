class Effect:
    def __init__(self, effect_dict: dict) -> None:
        self.hp = effect_dict.get("hp", 0)
        self.power = effect_dict.get("power", 0)
        self.protection = effect_dict.get("protection", 0)
