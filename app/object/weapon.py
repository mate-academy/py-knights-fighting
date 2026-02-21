class Weapon:

    def __init__(self, weapon_name: str, weapon_power: int) -> None:
        self.name = weapon_name
        self.power = weapon_power

    def __repr__(self) -> str:
        return f"<Weapon name: {self.name}, Weapon power: {self.power}>"
