class Armour:
    def __init__(self, armour_type: str, protection: int):
        self.armour_type = armour_type
        self.protection = protection

    @staticmethod
    def create_armour(armour_dict):
        return Armour(armour_dict['part'], armour_dict['protection'])
