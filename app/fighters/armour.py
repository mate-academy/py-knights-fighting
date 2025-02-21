class Armour:
    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return f"Armour({self.part}, protection={self.protection})"
