class Armor:
    def __init__(self) -> None:
        self.helmet = 0
        self.breast = 0
        self.boots = 0


class Weapon:
    def __init__(self, right_hand: int) -> None:
        self.right = right_hand
        self.left = 0
