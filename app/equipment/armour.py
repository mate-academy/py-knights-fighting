class Armour:
    armours_arr = {}

    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

        if self.part not in Armour.armours_arr:
            Armour.armours_arr[self.part] = self
