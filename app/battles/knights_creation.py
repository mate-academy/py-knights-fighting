from app.knights.knight import Knight
from app.knights.armour import Armour
from app.knights.weapon import Weapon
from app.knights.potion import Potion
from app.main import KNIGHTS


class KnightsCreation:
    def __init__(self, knights_in_dictionary: dict) -> None:
        self.knights_in_dictionary = knights_in_dictionary

    def knight_create(self, knight_name: str) -> Knight:

        knight = Knight(
            self.knights_in_dictionary[knight_name]["name"],
            self.knights_in_dictionary[knight_name]["power"],
            self.knights_in_dictionary[knight_name]["hp"]
        )
        knight.armour = [
            Armour(unit["part"], unit["protection"])
            for unit in self.knights_in_dictionary[knight_name]["armour"]
        ]
        knight.power = Weapon(
            self.knights_in_dictionary[knight_name]["weapon"]["name"],
            self.knights_in_dictionary[knight_name]["weapon"]["power"]
        )
        if self.knights_in_dictionary[knight_name]["potion"]:
            knight.potion = Potion(
                self.knights_in_dictionary[knight_name]["potion"]["name"],
                self.knights_in_dictionary[knight_name]["potion"]["effect"]
        )
        return knight


create = KnightsCreation(KNIGHTS)
KnightsCreation.knight_create(create, "lancelot")
