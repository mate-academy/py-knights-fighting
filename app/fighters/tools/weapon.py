class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def get_instance(cls, weapon: dict) -> "Weapon":
        return cls(name=weapon["name"], power=weapon["power"])
