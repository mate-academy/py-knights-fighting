class Armor:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def apply_effect(self, stats: dict) -> dict:
        for stat, change in self.effect.items():
            stats[stat] = stats.get(stat, 0) + change
        return stats
