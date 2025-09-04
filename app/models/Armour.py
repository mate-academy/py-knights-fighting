class Armour:
    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

    @classmethod
    def from_dict(cls, data: dict):
        part = data.get("part")
        protection = data.get("protection")
        return cls(part, protection)

