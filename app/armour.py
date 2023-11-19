class Armour:
    def __init__(self, config: list[dict]) -> None:
        self.protection = sum([part["protection"] for part in config])
