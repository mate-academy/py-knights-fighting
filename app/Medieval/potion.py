class Effect:
    def __init__(self) -> None:
        pass

    def get_effect(self, potion_effect: dict) -> None:
        if "power" in potion_effect:
            self.power = potion_effect["power"]
        if "hp" in potion_effect:
            self.hp = potion_effect["hp"]
        if "protection" in potion_effect:
            self.protection = potion_effect["protection"]


class Potion:
    def __init__(self, name: str, effect: Effect) -> None:
        self.name = name
        self.effect = effect
