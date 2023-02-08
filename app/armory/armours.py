class Armour:
    def __init__(
        self, name: str | None, part: str | None, protection: int | None
    ) -> None:
        self.name = name
        self.part = part
        self.protection = protection
