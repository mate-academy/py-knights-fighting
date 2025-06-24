class Knight:

    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict,
                 protection: int = 0) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion
        self.protection = protection
        self.add_protection()
        self.add_power_from_weapon()
        self.add_potion()

    def add_protection(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def add_power_from_weapon(self) -> None:
        self.power += self.weapon["power"]

    def add_potion(self) -> None:
        if self.potion:
            if "power" in self.potion["effect"]:
                self.power += self.potion["effect"]["power"]

            if "hp" in self.potion["effect"]:
                self.hp += self.potion["effect"]["hp"]

            if "protection" in self.potion["effect"]:
                self.protection += self.potion["effect"]["protection"]

    def fight(self, other: "Knight") -> None:
        self.hp = max(0, self.hp - other.power + self.protection)
        other.hp = max(0, other.hp - self.power + other.protection)


def battle(knightsconfig: dict) -> dict:
    dict_of_knights = {}
    for knight in knightsconfig:
        dict_of_knights[knight] = Knight(**knightsconfig[knight])
    dict_of_knights["lancelot"].fight(dict_of_knights["mordred"])
    dict_of_knights["arthur"].fight(dict_of_knights["red_knight"])
    return {knight.name: knight.hp for knight in dict_of_knights.values()}
