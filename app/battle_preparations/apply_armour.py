class Armour:
    @staticmethod
    def armour_protection(armors: list) -> int:
        return sum(
            [
                armor["protection"] for armor in armors
                if len(armors) != 0
            ]
        )
