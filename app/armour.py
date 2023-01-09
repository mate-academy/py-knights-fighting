from knight import Knight


class Armour:
    """Class adds armour protection to the knight"""

    @staticmethod
    def get_armour(armour: list) -> None:
        """Method adds armour protection to the knight"""
        total_protection = 0
        for part in armour:
            total_protection += part["protection"]
        Knight.protection = total_protection
