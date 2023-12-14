class Potion:
    def __init__(self, potion_dict: dict) -> None:
        self.potion_dict = potion_dict

    def potion_score(self) -> dict:
        for name, characteristics in self.potion_dict.items():
            if characteristics["potion"]:
                for key_2, value_2 \
                        in characteristics["potion"]["effect"].items():
                    characteristics[key_2] \
                        += characteristics["potion"]["effect"][key_2]
        return self.potion_dict
