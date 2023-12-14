class Potion:
    def __init__(self, potion_dict: dict) -> None:
        self.potion_dict = potion_dict

    def potion_score(self) -> dict:
        for potion in self.potion_dict:
            if self.potion_dict[potion]["potion"]:
                for effect in self.potion_dict[potion]["potion"]["effect"]:
                    self.potion_dict[potion][effect] += (
                        self.potion_dict)[potion]["potion"]["effect"][effect]
        return self.potion_dict
