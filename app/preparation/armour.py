class Armor:
    def __init__(self, warrior: dict) -> None:
        self.warrior = warrior

    def put_on_armour(self) -> None:
        # apply armor
        self.warrior["protection"] = 0
        for part in self.warrior["armour"]:
            self.warrior["protection"] += part["protection"]
