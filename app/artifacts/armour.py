class Armour:
    def __init__(self, config: list[dict]) -> None:
        if config:
            self.protection = sum([part["protection"] for part in config])
        else:
            self.protection = 0
