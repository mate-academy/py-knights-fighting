class Armour:
    def __init__(self, armour_dict: dict) -> None:
        self.armour_dict = armour_dict

    def armor_score(self) -> dict:
        for value in self.armour_dict:
            self.armour_dict[value]["protection"] = 0
            if self.armour_dict[value]["armour"]:
                for armour in self.armour_dict[value]["armour"]:
                    self.armour_dict[value]["protection"] \
                        += armour["protection"]
        return self.armour_dict
