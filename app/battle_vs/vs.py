class VS:
    def __init__(self, knights_config: dict, other: dict) -> None:
        self.knights_config = knights_config
        self.other = other
        self.knights_config["hp"] -= \
            self.other["power"] - self.knights_config["protection"]
