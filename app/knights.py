class Potion():
    potion_list = []

    def __init__(self, name: str, power: int, hp: int,
                 protection: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection
        Potion.potion_list.append(self)


class Knights():
    knights_list = []

    def __init__(self, name: str, power: int, hp: int,
                 armour: list, weapon: dict,
                 potion: (Potion, None)) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        Knights.knights_list.append(self)

    def apply_armour(self) -> None:
        for part in self.armour:
            self.protection += part["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            self.power += self.potion.power
            self.hp += self.potion.hp
            self.protection += self.potion.protection

    def fight_preparing(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()


def create_knight(knights_info: dict) -> None:

    for knight in knights_info:
        if (knights_info[knight]["potion"] is not None):
            power, hp, protection = 0, 0, 0

            if "power" in knights_info[knight]["potion"]["effect"]:
                power += knights_info[knight]["potion"]["effect"]["power"]
            if "hp" in knights_info[knight]["potion"]["effect"]:
                hp += knights_info[knight]["potion"]["effect"]["hp"]
            if "protection" in knights_info[knight]["potion"]["effect"]:
                protection = knights_info[knight]["potion"]["effect"][
                    "protection"]

            potion = Potion(knights_info[knight]["potion"]["name"],
                            power, hp, protection)
        else:
            potion = None

        Knights(knights_info[knight]["name"],
                knights_info[knight]["power"],
                knights_info[knight]["hp"],
                knights_info[knight]["armour"],
                knights_info[knight]["weapon"],
                potion)
