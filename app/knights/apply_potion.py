class Potion:
    def __init__(self, knight: dict) -> None:
        self.knight = knight

    def apply_potion(self) -> dict:
        for hero in self.knight:
            if self.knight[hero]["potion"] is not None:
                Potion(self.knight[hero]).add_parameters()
        return self.knight

    def add_parameters(self) -> dict:
        for add in self.knight["potion"]["effect"]:
            if add in self.knight["potion"]["effect"]:
                self.knight[add] += self.knight["potion"]["effect"][add]
        return self.knight
