class Weapon:
    def __init__(self, parameters: dict) -> None:
        self.name = parameters["name"]
        self.power = parameters["power"]

    def __repr__(self) -> str:
        return f"{self.name} {self.power}"

    def __str__(self) -> str:
        return f"{self.name} {self.power}"
