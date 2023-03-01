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
    def create_the_knight(knights: dict) -> dict:
        for knight in knights.values():
            Knight.knights[knight["name"]] = Knight(
                knight["name"], knight["power"], knight["hp"])
        return Knight.knights

    def check_fell(self):
        if self.hp <= 0:
            self.hp = 0
