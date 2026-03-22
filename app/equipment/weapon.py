from app.warrior.stats import Stats


class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self.name = weapon_dict["name"]
        self.stats = Stats(power=weapon_dict["power"])
