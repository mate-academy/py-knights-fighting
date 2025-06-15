from app.battle_field.stats import Stats


class Potion:
    def __init__(self, potion_name: str, potion_power: int, potion_hp: int, potion_protection: int) -> None:
        self.name = potion_name
        self.power = potion_power
        self.hp = potion_hp
        self.protection = potion_protection

    def get_stats(self) -> Stats:
        return Stats(self.hp, self.power, self.protection)
