class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self.weapon_dict = weapon_dict

    def weapon_score(self) -> dict:
        for i in self.weapon_dict:
            if self.weapon_dict[i]["weapon"]:
                self.weapon_dict[i]["power"] +=\
                    self.weapon_dict[i]["weapon"]["power"]
        return self.weapon_dict
