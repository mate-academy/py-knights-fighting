class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply_effect(self, knight: object) -> None:
        if "hp" in self.effect:
            knight.hp += self.effect["hp"]
        if "power" in self.effect:
            knight.power += self.effect["power"]
        if "protection" in self.effect:
            knight.total_protection += self.effect["protection"]
