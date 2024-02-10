class Knight:

    def __init__(self):
        self.name = ''
        self.base_power = 0
        self.base_hp = 0
        self.protection = 0
        self.armour = []
        self.weapon = {}
        self.potion = {}

    def return_properties(self) -> dict:
        return {'name': self.name,
            'hp': self.base_hp,
            'power': self.base_power,
            'protection': self.protection
            }