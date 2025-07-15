class Armour:
    def __init__(self, armour_dict: dict[str, str | int]) -> None:
        self.part: str = armour_dict.get("part")
        self.protection: str = armour_dict.get("protection")
