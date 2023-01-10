class Potion:

    potions = {}

    def __init__(self, name: str = None, power: int = 0,
                 health: int = 0, protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.health = health
        self.protection = protection
        self.__class__.potions[self.name] = self
