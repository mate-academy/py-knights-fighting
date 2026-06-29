class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


def create_armour_instances(armours: list[dict]) -> list[Armour]:
    return [
        Armour(part=armour["part"], protection=armour["protection"])
        for armour in armours
    ]
