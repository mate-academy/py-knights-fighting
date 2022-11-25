class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = None
        self.power = 0
        for key in weapon:
            setattr(self, key, weapon[key])
