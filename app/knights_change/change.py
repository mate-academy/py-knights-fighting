from app.knights_change.knights import Armour, Weapon, Potion, Knights


def from_dict(knight_dict: dict) -> Knights:
    result = ''
    for name, values in knight_dict.items():
        knight = Knights(**values)
        for key, value in values.items():
            if key == "armour":
                ar = [Armour(**arm) for arm in value]
                setattr(knight, key, ar)
            if key == "weapon":
                setattr(knight, key, Weapon(**value))
            if key == "potion":
                if value is not None:
                    pot = Potion(value["name"], **value["effect"])
                    setattr(knight, key, pot)
        result = knight
    return result