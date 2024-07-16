class Knights:

    knights = {}

    def __init__(
            self, name: str, hp: int,
            power: int, protection: int
    ) -> None:
        self.name = name
        self.hp = hp
        self.power = power
        self.protection = protection
        Knights.knights[self.name] = self
        print(
            f"""
            {self.name} was created!
            hp={self.hp} power={self.power} protection={self.protection}
            """
        )


def create_knight(name: str, knights: dict) -> Knights:
    return Knights(name, *knights[name])


def current_knights_hps() -> dict:
    return {name: data.hp for name, data in Knights.knights.items()}
