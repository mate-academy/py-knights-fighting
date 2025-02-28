class Weapon:
    def __init__(self, weapon_data: dict) -> None:
        self.name: str = weapon_data["name"]
        self.power: int = weapon_data["power"]
