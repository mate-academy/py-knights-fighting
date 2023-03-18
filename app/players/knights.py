class Knights:
    def __init__(
            self,
            noble_name: str,
            hp: int,
            power: int,
            protection: int = 0
    ) -> None:
        self.noble_name = noble_name
        self.hp = hp
        self.power = power
        self.protection = protection
