class Armour:
    """Armour item that protects a specific body part."""

    part: str
    protection: int

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection
