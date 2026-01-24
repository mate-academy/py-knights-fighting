class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    @classmethod
    def create_weapon_from_dict(cls,
                                dictionary: dict) -> "Weapon":
        return cls(name=dictionary["name"],
                   power=dictionary["power"])
