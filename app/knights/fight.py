from app.knights.characters import Knight


class Fight:
    def __init__(self, first: Knight, second: Knight) -> None:
        self.first = first
        self.second = second
        self.first.activate_items()
        self.second.activate_items()

    def fight_hit(self) -> None:
        self.first.hp -= self.second.power - self.first.protection
        self.second.hp -= self.first.power - self.second.protection
        if self.first.hp < 0:
            self.first.hp = 0
        if self.second.hp < 0:
            self.second.hp = 0
