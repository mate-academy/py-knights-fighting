class Potion:
    def __init__(self, parameters: dict) -> None:
        self.name = parameters["name"]
        self.power = parameters["effect"].get("power", 0)
        self.hp = parameters["effect"].get("hp", 0)
        self.protection = parameters["effect"].get("protection", 0)

    def __repr__(self) -> str:
        return f"Potion {self.name}"

    def __str__(self) -> str:
        return f"{self.name.upper()} Potion"
