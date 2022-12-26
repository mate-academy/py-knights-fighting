class Potion:
    def __init__(self, name: str = None, effect: dict = {"power": 15, "hp": -5, "protection": 10}):
        self.name = name
        self.effect = effect

    def get_effect_on_power(self):
        return self.effect.get("power", 0)

    def get_effect_on_hp(self):
        return self.effect.get("hp", 0)

    def get_effect_on_protection(self):
        return self.effect.get("protection", 0)