class ArmourPart:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    def __repr__(self) -> str:
        return f"ArmourPart(part='{self.part}', protection={self.protection})"
