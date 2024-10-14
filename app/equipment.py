class Armour:
    def __init__(self, stats: dict) -> None:
        self.part = stats["part"]
        self.protection = stats["protection"]


class Weapon:
    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.power = stats["power"]


class Potion:
    def __init__(self, stats: dict) -> None:
        if stats:
            self.name = stats.get("name")
            self.effects = stats.get("effect")
