class Part:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Armour:
    def __init__(self, armour: list) -> None:
        self.armour = [Part(**part) for part in armour]
        self.protection = sum([part.protection for part in self.armour])
