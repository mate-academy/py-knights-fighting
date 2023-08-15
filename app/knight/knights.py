class Knights:
    def __init__(
        self,
        name: str,
        name_in_dict: str,
        power: int,
        hp: int,
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.name_in_dict = name_in_dict
        self.protection = 0
