class Knight:

    knights = {}

    def __init__(self, name, power, hp, protection=0):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    def __repr__(self):
        return f"{self.name}"

    @staticmethod
    def create_the_knight(persons: dict) -> dict:
        for pers in persons.values():
            Knight.knights[pers["name"]] = Knight(
                pers["name"], pers["power"], pers["hp"])
        return Knight.knights

    def check_fell(self):
        if self.hp <= 0:
            self.hp = 0
