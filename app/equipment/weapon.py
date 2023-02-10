class Weapon:
    weapons_arr = {}

    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power

        if self.name not in Weapon.weapons_arr:
            Weapon.weapons_arr[self.name] = self
