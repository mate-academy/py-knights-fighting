from app.base_information import KNIGHTS


class Knight:
    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def __repr__(self):
        return (f"[Knight {self.name}, stats and equipment: power = {self.power},\n "
                f"health points = {self.hp}, armour = {self.armour}, total protection = {self.protection},\n "
                f"weapons = {self.weapon},potions = {self.potion}]\n")

def dict_into_cls(candid: dict) -> Knight:
    lst_of_knights = []
    for knight, stats in candid.items():
        x = globals()[knight] = Knight(**stats)
        lst_of_knights.append(x)
    return lst_of_knights

knight_instances = dict_into_cls(KNIGHTS)
