class Potion:
    def __init__(self, name: str, effect: bool) -> None:
        self.name = name
        self.effect = effect

    def apply(self, knight: dict) -> None:
        if self.effect:
            if "power" in self.effect:
                knight.power += self.effect["power"]
            if "protection" in self.effect:
                knight.protection += self.effect["protection"]
            if "hp" in self.effect:
                knight.hp += self.effect["hp"]

    def __repr__(self) -> None:
        return f"Potion({self.name}, Effect: {self.effect})"
