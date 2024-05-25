from app.knight_properties.potion import Potion


def dict_to_potion(value: dict) -> Potion:
    potion = value["potion"]
    if value["potion"]:
        potion = Potion(value["potion"]["name"], value["potion"]["effect"])
    return potion
