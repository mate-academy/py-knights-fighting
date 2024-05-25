class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


def dict_to_potion(value: dict) -> Potion:
    if value["potion"]:
        return Potion(value["potion"]["name"], value["potion"]["effect"])
    return value["potion"]
