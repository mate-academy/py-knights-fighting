class Weapon:
    def __init__(self, weapon_dict: dict) -> None:
        self.weapon_dict = weapon_dict

    def weapon_score(self) -> dict:
        for name, characteristics in self.weapon_dict.items():
            if characteristics["weapon"]:
                characteristics["power"] +=\
                    characteristics["weapon"]["power"]
        return self.weapon_dict
