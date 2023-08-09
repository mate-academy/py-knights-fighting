class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_element(cls, item_set: dict) -> "Armour":
        return cls(
            part=item_set["part"],
            protection=item_set["protection"]
        )
