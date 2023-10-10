class Potion:
    def __init__(self, potion_info: dict) -> None:
        self.name = potion_info["name"]
        self.effect = potion_info["effect"]
