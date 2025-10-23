class Armour:

    def __init__(self, part: str, protection: int):
        self.part = part
        self.protection = protection

    def weapon(self):
        return {"part": self.part,
                "protection": self.protection}