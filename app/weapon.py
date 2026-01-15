class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self.weapon_dict = weapon_dict

    def weapon_score(self) -> dict:
        for name, power in self.weapon_dict.items():
            if power["weapon"]:
                power["power"] +=\
                    power["weapon"]["power"]
        return self.weapon_dict
