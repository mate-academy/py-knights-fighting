class Weapon:
    def __init__(self, name: str, power: str) -> None:
        self.name = name
        self.power = power

    @classmethod
    def weapon_registration(cls, knights_weapons: dict) -> "Weapon":
        return cls(knights_weapons["name"], knights_weapons["power"])
