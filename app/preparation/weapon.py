class Weapon:
    def __init__(self, warrior: dict) -> None:
        self.warrior = warrior

    def tool_up(self) -> None:
        # apply weapon
        self.warrior["power"] += self.warrior["weapon"]["power"]
