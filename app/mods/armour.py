class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


def get_armours(armours: list) -> list[Armour]:
    armours_list = []
    for armor in armours:
        armours_list.append(
            Armour(
                armor["part"],
                armor["protection"],
            )
        )
    return armours_list
