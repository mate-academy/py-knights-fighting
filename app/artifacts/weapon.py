from app.battle_field.stats import Stats


class Weapon:
    def __init__(self, weapon_name: str, weapon_power: int) -> None:
        self.name = weapon_name
        self.power = weapon_power

    def get_stats(self) -> Stats:
        return Stats(0, self.power, 0)
