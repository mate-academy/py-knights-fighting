class Potion:
    def __init__(self, config: dict) -> None:
        if config is not None:
            self.is_potion = True
            self.name = config["name"]
            self.effect = config["effect"]
        else:
            self.is_potion = False
