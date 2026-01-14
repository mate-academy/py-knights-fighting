class Weapon:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    @classmethod
    def from_dict(cls, data: dict):
        name = data.get("name", )
        power = data.get("power", 0)
        return cls(name, power)

    
