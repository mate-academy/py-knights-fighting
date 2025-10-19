class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_dict(cls, data: dict) -> "Armour":
        return cls(
            part=data["part"],
            protection=data["protection"]
        )
