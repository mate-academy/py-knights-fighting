class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @staticmethod
    def armour_registration(knights_armour: list[dict]) -> list["Armour"]:
        return [
            Armour(part["part"], part["protection"]) for part in knights_armour
        ]
