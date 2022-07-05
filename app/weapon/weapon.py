class Weapon:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __repr__(self):
        return self.name

    # create a Weapon instance from dictionary with properties
    @classmethod
    def get_weapon_cls(cls, weapon: dict) -> "Weapon":
        return cls(
            name=weapon["name"],
            power=weapon["power"]
        )
