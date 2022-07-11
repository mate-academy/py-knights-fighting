class Armour():
    """ Class describe armour"""
    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

    @staticmethod
    def create_armour(armour: dict):
        return Armour(armour["part"], armour["protection"])
