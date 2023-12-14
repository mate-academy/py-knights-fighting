class Potion:
    def __init__(self, potion_dict: dict) -> None:
        self.potion_dict = potion_dict

    def potion_score(self) -> dict:
        for key, value in self.potion_dict.items():
            if value["potion"]:
                for key_2, value_2 in value["potion"]["effect"].items():
                    value[key_2] += value["potion"]["effect"][key_2]
        return self.potion_dict
