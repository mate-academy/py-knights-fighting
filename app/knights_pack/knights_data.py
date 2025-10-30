class Knight:
    def __init__(self, name: str,
                 knight_hp: int,
                 knight_power: int,
                 knight_protection: int,
                 ) -> None :
        self.name = name
        self.knight_hp = knight_hp
        self.knight_power = knight_power
        self.knight_protection = knight_protection

    def print_data(self) -> dict:
        return {self.name: self.knight_hp}
