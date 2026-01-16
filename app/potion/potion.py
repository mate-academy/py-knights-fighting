class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def get_power(self) -> int:
        return self.effect["power"]

    def get_hp(self) -> int:
        return self.effect["hp"]

    def get_protection(self) -> int:
        return self.effect["protection"] if "protection" in self.effect else 0
