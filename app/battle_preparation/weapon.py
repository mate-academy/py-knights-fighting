class Weapon:
    def __init__(self, weapon: dict) -> None:
        self.name = weapon["name"]
        self.power = weapon["power"]

    def __str__(self) -> str:
        return f"{self.name} weapon with power {self.power}"
