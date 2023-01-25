class Character:
    knight_list = {}

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            protection: int
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        Character.knight_list[self.name] = self
