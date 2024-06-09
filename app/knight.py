import app.gear as gear


class Knight:
    def __init__(self, knihgt_info: dict) -> None:
        self.name = knihgt_info["name"]
        self.power = knihgt_info["power"]
        self.hp = knihgt_info["hp"]
        self.protection = 0
        self.info = knihgt_info

    def apply_gear(self) -> None:
        gear.apply_armor(self)
        gear.apply_weapon(self)
        gear.apply_potion(self)


def apply_gear(knihgt_info: dict) -> None:
    gear.apply_armor(knihgt_info)
    gear.apply_weapon(knihgt_info)
    gear.apply_potion(knihgt_info)


def duel(white_knihgt: dict, bleak_knihgt: dict) -> None:
    white_knihgt["hp"] -= bleak_knihgt["power"] - white_knihgt["protection"]
    bleak_knihgt["hp"] -= white_knihgt["power"] - bleak_knihgt["protection"]

    # check if someone fell in battle
    if white_knihgt["hp"] <= 0:
        white_knihgt["hp"] = 0

    if bleak_knihgt["hp"] <= 0:
        bleak_knihgt["hp"] = 0
