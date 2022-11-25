class Armour:
    def __init__(self, armour_dict: dict) -> None:
        self.name = None
        self.protection = 0
        for armour in armour_dict:
            setattr(self, armour, armour_dict[armour])
