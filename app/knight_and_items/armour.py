class Armour:

    def __init__(self, stats: dict) -> None:
        self.part = stats.get("part")

        if stats.get("protection") is not None:
            self.protection = stats.get("protection")
        else:
            self.protection = 0
