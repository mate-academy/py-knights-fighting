class Weapon:
    def __init__(self):
        pass

    @staticmethod
    def get_weapon(weapon: dict) -> int:
        return weapon["power"]
