class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


def apply_armor(knihgt: dict) -> None:
    knihgt["protection"] = 0
    for armour in knihgt["armour"]:
        knihgt["protection"] += armour["protection"]


def apply_weapon(knihgt: dict) -> None:
    knihgt["power"] += knihgt["weapon"]["power"]


def apply_potion(knihgt: dict) -> None:
    if knihgt["potion"] is None:
        return
    if "power" in knihgt["potion"]["effect"]:
        knihgt["power"] += knihgt["potion"]["effect"]["power"]

    if "protection" in knihgt["potion"]["effect"]:
        knihgt["protection"] += knihgt["potion"]["effect"]["protection"]

    if "hp" in knihgt["potion"]["effect"]:
        knihgt["hp"] += knihgt["potion"]["effect"]["hp"]
