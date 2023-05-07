class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def armour_registration(cls, knights_armour: list[dict]) -> list["Armour"]:
        return [
            cls(part["part"], part["protection"]) for part in knights_armour
        ]
