class Armour:

    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


helmet = Armour("helmet", 15)
breastplate = Armour("breastplate", 20)
boots = Armour("boots", 10)
