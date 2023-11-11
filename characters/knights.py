class Knights:
    heroes = {}

    def __init__(self, stats: dict) -> None:
        self.name = stats["name"]
        self.power = stats["power"]
        self.hp = stats["hp"]
        self.protection = 0

        Knights.heroes[stats["name"]] = self
