class RegistrationKnight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict,
                 ):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = 0


def reg_knight(challenger: dict):
    fighters = {}
    for knight, stats in challenger.items():
        fighters[knight] = RegistrationKnight(
            stats["name"],
            stats["power"],
            stats["hp"],
            stats["armour"],
            stats["weapon"],
            stats["potion"],
        )
    return fighters
