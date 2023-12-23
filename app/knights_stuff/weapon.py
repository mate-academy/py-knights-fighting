class Weapon:
    def __init__(self) -> None:
        pass

    def weapon_power(self, weapon: dict[str, any]) -> int:
        return weapon["power"]
