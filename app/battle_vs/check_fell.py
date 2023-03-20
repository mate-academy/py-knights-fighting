class CheckFell:
    def __init__(self, knights_config: dict) -> None:
        self.knights_config = knights_config
        if self.knights_config["hp"] <= 0:
            self.knights_config["hp"] = 0
