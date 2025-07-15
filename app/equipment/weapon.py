class Weapon:
    def __init__(self, weapon_dict: dict[str, str | int]) -> None:
        self.name: str = weapon_dict.get("name")
        self.power: int = weapon_dict.get("power")
