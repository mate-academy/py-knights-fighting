class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect

    def if_effect_exist_return_value(self, effect_name: str) -> int:
        if effect_name in self.effect:
            return self.effect[effect_name]

        return 0


def get_potion_instance(potion: dict) -> None | Potion:
    if not potion:
        return None
    return Potion(potion["name"], potion["effect"])
