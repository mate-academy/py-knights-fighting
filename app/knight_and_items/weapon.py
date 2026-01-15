class Weapon:

    def __init__(self, stats: dict) -> None:
        self.name = stats.get("name")
        self.power = stats.get("power")
