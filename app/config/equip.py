class Armour:
    def __init__(self, list_armour: dict):
        self.list_armour = list_armour
        self.point_of_armour = 0

    def get_armour(self) -> int:
        for part in self.list_armour:
            if "protection" in part:
                self.point_of_armour += part["protection"]
        return self.point_of_armour


class Weapon:
    @staticmethod
    def get_weapon(weapon: dict) -> int:
        return weapon["power"]
