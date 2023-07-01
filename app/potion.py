class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def get_power(self):
        return self.effect.get("power", 0)

    def get_protection(self):
        return self.effect.get("protection", 0)

    def get_hp(self):
        return self.effect.get("hp", 0)
