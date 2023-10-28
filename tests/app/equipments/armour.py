class Armour:

    def __init__(self, armour: list) -> None:
        self.armour = armour

    def get_protection_value(self) -> int:
        """
        calculates the total protection value
        :return: additional protect
        """
        return sum([unit["protection"] for unit in self.armour])
