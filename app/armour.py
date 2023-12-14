from app.weapon import Weapon


class Armour:
    def __init__(self, armour_dict: dict) -> None:
        self.armour_dict = armour_dict

    def armor_score(self) -> dict:
        for key, value in self.armour_dict.items():
            value["protection"] = 0
            if value["armour"]:
                value["protection"] += (
                    sum(num["protection"] for num in value["armour"]))
        weapon = Weapon(self.armour_dict)
        return weapon.weapon_score()
