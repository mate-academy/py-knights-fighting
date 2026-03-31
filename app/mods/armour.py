class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


def get_armours(armours: list) -> list[Armour]:
    return [Armour(**armor) for armor in armours]
