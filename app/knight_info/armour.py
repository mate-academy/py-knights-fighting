class Armour:
    @staticmethod
    def total_armour(armours: list) -> int:
        return sum(armour["protection"] for armour in armours)
