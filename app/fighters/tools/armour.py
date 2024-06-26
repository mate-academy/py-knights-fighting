class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


def get_armour_instances(armours: list) -> list[Armour]:
    return [Armour(armour["part"], armour["protection"])
            for armour in armours]
