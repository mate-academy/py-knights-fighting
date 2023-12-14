class Potion:
    def __init__(self, potion_dict: dict) -> None:
        self.potion_dict = potion_dict

    def potion_score(self) -> dict:
        for name, potion in self.potion_dict.items():
            if potion["potion"]:
                way_effect = potion["potion"]["effect"]
                for effect_key, effect in way_effect.items():
                    potion[effect_key] += way_effect[effect_key]
        return self.potion_dict
