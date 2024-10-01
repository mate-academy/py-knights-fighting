class KnightPotion:
    def __init__(self, name: str, effect: dict):
        self.name = name
        self.effect = effect

    def get_hp(self):
        return self.effect["hp"] if "hp" in self.effect else 0

    def get_power(self):
        return self.effect["power"] if "power" in self.effect else 0

    def get_protection(self):
        return self.effect["protection"] if "protection" in self.effect else 0