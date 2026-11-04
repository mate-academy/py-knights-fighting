class Hp:
    def __init__(self, base_hp: int) -> None:
        self.hp = base_hp

    def add_hp(self, add_hp: int) -> None:
        self.hp += add_hp
