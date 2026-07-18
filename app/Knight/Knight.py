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

    def __repr__(self) -> str:
        return (f"[Knight {self.name}, stats and equipment: "
                f"power = {self.power},\n "
                f"health points = {self.hp}, "
                f"armour = {self.armour}, "
                f"total protection = {self.protection},\n "
                f"weapons = {self.weapon},"
                f"potions = {self.potion}]\n")


def dict_into_cls(candid: dict) -> list[Knight]:
    lst_of_knights = []
    lancelot = Knight(**candid["lancelot"])
    lst_of_knights.append(lancelot)
    arthur = Knight(**candid["arthur"])
    lst_of_knights.append(arthur)
    mordred = Knight(**candid["mordred"])
    lst_of_knights.append(mordred)
    red_knight = Knight(**candid["red_knight"])
    lst_of_knights.append(red_knight)
    return lst_of_knights
