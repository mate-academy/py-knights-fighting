class Armour:
    def __init__(self, armour_pieces: list[dict]) -> None:
        for armour_piece in armour_pieces:
            setattr(self, armour_piece["part"], armour_piece["protection"])

    def total_equipment_protection(self) -> int:
        return sum(self.__dict__.values())