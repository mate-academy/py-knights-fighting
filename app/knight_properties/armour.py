class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


def dict_to_armour(value: dict) -> list[Armour]:
    armour = []
    if len(value["armour"]):
        return [
            Armour(
                armour_item["part"],
                armour_item["protection"]
            )
            for armour_item in value["armour"]
        ]
    return armour
