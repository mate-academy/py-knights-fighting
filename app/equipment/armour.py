class Armour:
    def __init__(self, armour: list[dict] = None) -> None:
        self.protection = 0
        if armour is not None:
            for item in armour:
                self.protection += item.get("protection")
