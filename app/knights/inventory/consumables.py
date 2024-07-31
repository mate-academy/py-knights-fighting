class Effects:
    def __init__(self, effect):
        if "power" in effect:
            self.power = effect["power"]
        if "protection" in effect:
            self.protection = effect["protection"]
        if "hp" in effect:
            self.hp = effect["hp"]


class Potion:
    def __init__(self, potion: dict):
        self.name = potion["name"]
        self.effect = Effects(potion["effect"])

    @classmethod
    def add(cls, potion: dict):
        if potion is None or potion == "None":
            return None
        return cls(potion)
