from app.knight_stats import KNIGHTS


class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict,
                 protection: int = 0):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection

    def equip(self):
        for piece_of_armor in self.armour:
            self.protection += piece_of_armor["protection"]
        self.power += self.weapon["power"]
        return self

    def drink_potion(self):
        if self.potion is not None:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            return self

    def challenge(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection

        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} says: \"Oh no, I\'m dead ;(\"")
        else:
            print(f"{self.name} says: \"DIZ BUT A SCRATCH!!!\"")

        if other.hp <= 0:
            other.hp = 0
            print(f"{other.name} says: \"Oh no, I\'m dead ;(\"")

        else:
            print(f"{other.name} says: \"DIZ BUT A SCRATCH!!!\"")


def get_knight(knight_name: dict):
    return Knight(
                  KNIGHTS[knight_name]["name"],
                  KNIGHTS[knight_name]["power"],
                  KNIGHTS[knight_name]["hp"],
                  KNIGHTS[knight_name]["armour"],
                  KNIGHTS[knight_name]["weapon"],
                  KNIGHTS[knight_name]["potion"]
    )
