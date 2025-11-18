class Armor:
    def __init__(self, armor: dict) -> None:
        self.part = armor.get("part", "")
        self.protection = armor.get("protection", 0)
