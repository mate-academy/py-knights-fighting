class Weapon:
    def __init__(self, data: dict[str, int]) -> None:
        self.name = data["name"]
        self.power = data["power"]
