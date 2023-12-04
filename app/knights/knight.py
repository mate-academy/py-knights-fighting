from app.knights.armors import Armour, Weapon, Potion


class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp


def knight_create(knights_in_dictionary: dict, knight_name: str) -> Knight:
    knight = Knight(
        knights_in_dictionary[knight_name]["name"],
        knights_in_dictionary[knight_name]["power"],
        knights_in_dictionary[knight_name]["hp"]
    )
    knight.armour = [
        Armour(unit["part"], unit["protection"])
        for unit in knights_in_dictionary[knight_name]["armour"]
    ]
    knight.weapon = Weapon(
        knights_in_dictionary[knight_name]["weapon"]["name"],
        knights_in_dictionary[knight_name]["weapon"]["power"]
    )
    if knights_in_dictionary[knight_name]["potion"]:
        knight.potion = Potion(
            knights_in_dictionary[knight_name]["potion"]["name"],
            knights_in_dictionary[knight_name]["potion"]["effect"]
        )
    return knight
