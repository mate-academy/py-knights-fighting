class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def get_protection(self) -> int:
        return self.protection
