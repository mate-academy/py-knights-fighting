class Armour:
    armours_arr = {}

    def __init__(self, name: str, part: str, protection: int) -> None:
        self.name = name
        self.part = part
        self.protection = protection

        if self.part not in Armour.armours_arr:
            Armour.armours_arr[self.name] = self
