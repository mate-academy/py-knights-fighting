from app.keys import KeysWeapon


class Weapon:
    def __init__(self, dict_weapon: dict) -> None:
        self.name = dict_weapon[KeysWeapon.NAME.value]
        self.power = dict_weapon[KeysWeapon.POWER.value]
