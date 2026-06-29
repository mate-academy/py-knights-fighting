class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


def create_weapon_instance(weapon: dict) -> Weapon:
    return Weapon(name=weapon["name"], power=weapon["power"])
