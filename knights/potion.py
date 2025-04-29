class Potion:
    def __init__(self, potion_config: dict) -> None:
        self.name = potion_config["name"]
        self.effect = potion_config["effect"]
