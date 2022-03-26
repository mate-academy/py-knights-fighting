class Weapon():

    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    @staticmethod
    def create_weapons(weapon: dict):
        return Weapon(weapon["name"], weapon["power"])
