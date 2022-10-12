class Armour:
    def __init__(self, list_of_armour: list):
        self.list_of_armour = list_of_armour
        self.applied_armor = 0

    def get_armour(self) -> int:
        for part in self.list_of_armour:
            self.applied_armor += part["protection"]
        return self.applied_armor
