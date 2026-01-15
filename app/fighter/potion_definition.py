class Potion:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def count_effect(self) -> tuple:
        power = self.effect["power"]
        hp = self.effect["hp"]
        if self.effect.get("protection", None):
            protection = self.effect["protection"]
        else:
            protection = 0
        return power, hp, protection
