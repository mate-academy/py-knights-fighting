class Armour:
    """
    Class of single Armour that equipped on knight

    Usually each instance of knight has several armour
    """

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection

    @classmethod
    def from_element(cls, item_set: dict) -> "Armour":
        return cls(
            part=item_set["part"],
            protection=item_set["protection"]
        )
