class Weapon:

    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def weapon(self):
        return {"name": self.name,
                "power": self.power}
