class Weapon:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    @staticmethod
    def create_weapon(weapon_dict):
        return Weapon(weapon_dict['name'], weapon_dict['power'])
