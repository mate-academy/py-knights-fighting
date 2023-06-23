class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:

    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def drink(self) -> tuple:
        hp = self.effect["hp"] if "hp" in self.effect.keys() else 0
        power = self.effect["power"] if "power" in self.effect.keys() else 0
        protection = (
            self.effect["protection"]
            if "protection" in self.effect.keys()
            else 0
        )
        return hp, power, protection
