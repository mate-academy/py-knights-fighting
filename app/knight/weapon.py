class Weapon:
    def __init__(self, parameters: dict) -> None:
        self.name = parameters["name"]
        self.power = parameters["power"]

    def __repr__(self):
        return f"{self.name} {self.power}"

    def __str__(self):
        return f"{self.name} {self.power}"
