class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

    def equip_weapon(self) -> int:
        return self.power
