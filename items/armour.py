class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __str__(self) -> str:
        return f"part: {self.part}, protect: {self.protection}"

    @staticmethod
    def create_armour(knight: dict) -> list["Armour"]:
        return [
            Armour(**part_arm)
            for part_arm in knight["armour"]
        ]
