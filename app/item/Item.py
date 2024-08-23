class Item:
    def __init__(self, name: str,
                 hp_bonus: int,
                 power_bonus: int,
                 protection_bonus: int) -> None:
        self.name = name
        self.hp_bonus = hp_bonus
        self.power_bonus = power_bonus
        self.protection_bonus = protection_bonus
