class Armour:
    def __init__(self, part: str, protection) -> None:
        self.part = part
        self.protection = protection

    def shine(self) -> str:
        return f"{self.part} shining!"
