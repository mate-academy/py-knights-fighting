class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 protection: int,
                 ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


def create_knight(knight: dict) -> Knight:
    knight = Knight(
        name=knight["name"],
        power=knight["power"],
        hp=knight["hp"],
        protection=0,
    )
    return knight
