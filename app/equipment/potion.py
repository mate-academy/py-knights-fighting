class Potion:
    def __init__(self, name: str, hp_buff: int | None,
                 power_buff: int | None, protection_buff: int | None) -> None:
        self.name = name
        self.hp_buff = hp_buff
        self.power_buff = power_buff
        self.protection_buff = protection_buff
