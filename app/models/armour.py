class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> None:
        return f"Armour({self.part}, Protection: {self.protection})"
