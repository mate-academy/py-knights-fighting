from app.models.armour import Armour


class Armours:
    def __init__(self, armours: list) -> None:
        if armours:
            self.armours = [Armour(**armour) for armour in armours]
        else:
            self.armours = []
