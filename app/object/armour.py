class Armour:

    def __init__(self, part_name: str, protection: int) -> None:
        self.name = part_name
        self.protection = protection

    def __repr__(self) -> str:
        return f"<Piece name: {self.name}, \
Piece protection: {self.protection}>"
