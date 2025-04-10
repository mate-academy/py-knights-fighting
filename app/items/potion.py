class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        if "power" in effect:
            self.power = effect["power"]
        else:
            self.power = 0
        if "hp" in effect:
            self.hp = effect["hp"]
        else:
            self.hp = 0
        if "protection" in effect:
            self.protection = effect["protection"]
        else:
            self.protection = 0
