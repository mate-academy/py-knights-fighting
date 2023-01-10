class Armour:

    armours = {}

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection
        self.__class__.armours[self.part + str(self.protection)] = self
