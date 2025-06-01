class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(
            self, name: str,
            power: int = 0,
            hp: int = 0,
            protection: int = 0
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection


class Knights:
    all_knights = {}

    def __init__(
            self, name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: "Weapon",
            potion: None | Potion
    ) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        Knights.all_knights[name] = self



# artur_armour = [
#     Armour("helmet", 15),
#     Armour("breastplate", 20),
#     Armour("boots", 10)
# ]
# mordred_armour = [
#     Armour("breastplate", 15),
#     Armour("boots", 10)
# ]
#
# lancelot = Knights(
#     "Lancelot",
#     35,
#     100,
#     [],
#     Weapon("Metal Sword", 50),
#     None
# )
# arthur = Knights(
#     "Arthur",
#     45,
#     75,
#     artur_armour,
#     Weapon("Two-handed Sword", 55),
#     None
# )
# mordred = Knights(
#     "Mordred",
#     30,
#     90,
#     mordred_armour,
#     Weapon("Poisoned Sword", 60),
#     Potion("Berserk", 15, -5, 10)
# )
# red_knight = Knights(
#     "Red Knight",
#     40,
#     70,
#     [Armour("breastplate", 25)],
#     Weapon("Two-handed Sword", 55),
#     Potion("Blessing", hp=10, power=5)
# )