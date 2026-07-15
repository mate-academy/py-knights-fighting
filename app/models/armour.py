class Armour:
    def __init__(self, armour_list: list) -> None:
        """
        Initializes the collection of armour parts.
        Accepts a list of dictionaries directly from the configuration data.
        """
        self.armour = armour_list or []

    def calculate_total_protection(self) -> int:
        """
        Sums up the protection value of all equipped armour parts.
        Returns 0 if no armour parts are present.
        """
        return sum(armour.get("protection", 0) for armour in self.armour)
