class Potion:
    def __init__(self, potion: dict | None) -> None:
        if potion is not None:
            self.name = potion["name"]
            self.hp = potion["effect"].get("hp", 0)
            self.power = potion["effect"].get("power", 0)
            self.protection = potion["effect"].get("protection", 0)
        else:
            self.name = "empty"
            self.hp = 0
            self.power = 0
            self.protection = 0

    def __str__(self) -> str:
        return (
            f"{self.name} potion  with effect {self.hp},"
            f"{self.power}, {self.protection} "
        )
