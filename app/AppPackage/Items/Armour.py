from typing import List


class Armour:
    def __init__(self, armour_data: List[dict] | None) -> None:
        self.helmet_protection: int = Armour.find_armour("helmet", armour_data)
        self.breastplate_protection: int = Armour.find_armour(
            "breastplate", armour_data
        )
        self.boots_protection: int = Armour.find_armour(
            "boots", armour_data
        )
        self.protection = (self.helmet_protection
                           + self.breastplate_protection
                           + self.boots_protection)

    @staticmethod
    def find_armour(armour_name: str, armour_data: List[dict]) -> int:
        """This method looks for specific armour in the list of dictionaries.
        If there are no armour with such name, it returns 0."""
        for armour in armour_data:
            if armour["part"] == armour_name:
                return armour["protection"]
        return 0
