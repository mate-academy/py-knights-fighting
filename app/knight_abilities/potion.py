class Potion:
    def __init__(self, name: str, effect: dict,
                 hp: int = 0, power: int = 0, protection: int = 0) -> None:
        self.name = name
        self.effect = effect
        self.hp = hp
        self.power = power
        self.protection = protection
        for key in self.effect:
            setattr(self, key, self.effect[key])
