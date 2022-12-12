from app.knights.knight import Knights


class Health:
    def __init__(self, hp1: Knights, hp2: Knights) -> None:
        self.hp1 = hp1
        self.hp2 = hp2

    def health(self) -> tuple:
        if self.hp1.hp < 0:
            self.hp1.hp = 0
        if self.hp2.hp < 0:
            self.hp2.hp = 0
        return self.hp1, self.hp2
