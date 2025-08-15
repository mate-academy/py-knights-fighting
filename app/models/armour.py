class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part: str = part
        self.protection: int = protection

    def __repr__(self) -> str:
        return f"Armour(part='{self.part}', protection={self.protection})"
