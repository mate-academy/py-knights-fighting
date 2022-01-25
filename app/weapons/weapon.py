class Weapon:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):
        return f"{self.name}"
