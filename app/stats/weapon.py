class Weapon:
    def __init__(self, name: str, power: str) -> None:
        self.name = name
        self.power = power

    @staticmethod
    def weapon_registration(knights_weapons: dir) -> "Weapon":
        return Weapon(knights_weapons["name"], knights_weapons["power"])
