class Armour:
    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

    def __repr__(self):
        return self.part

    # get the total points of armor
    @staticmethod
    def get_total_armour(protection: list) -> int:
        total_armour = 0
        if not protection:
            return 0

        for armour in protection:
            total_armour += armour["protection"]
        return total_armour
