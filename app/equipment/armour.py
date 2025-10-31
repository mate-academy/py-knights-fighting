class Armour:
    def __init__(self, armour: list[dict] = None) -> None:
        self.protection = 0
        for item in armour:
            if item.get("part") == "helmet":
                self.helmet = item.get("part")
                self.protection += item.get("protection")
            elif item.get("part") == "breastplate":
                self.breastplate = item.get("part")
                self.protection += item.get("protection")
            elif item.get("part") == "boots":
                self.boots = item.get("part")
                self.protection += item.get("protection")
