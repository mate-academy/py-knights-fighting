class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


def total_armour(armours: list[Armour]) -> int:
    return sum(armour.protection for armour in armours)
