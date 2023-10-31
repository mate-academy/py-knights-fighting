class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __str__(self) -> str:
        return f"part: {self.part}, protect: {self.protection}"

    @staticmethod
    def create_armour(name: str, config: dict) -> list["Armour"]:
        return [
            Armour(**part_armour)
            for part_armour in config[name]["armour"]
        ]
