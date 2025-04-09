class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self.name = name
        self.protection = protection

    def get_protection(self) -> int:
        return self.protection
