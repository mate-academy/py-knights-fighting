ItemValue = int | str


class Armour:
    def __init__(self, dict_of_armour: dict) -> None:
        self.part: str = dict_of_armour.get("part").title()
        self.protection = dict_of_armour.get("protection")


class Weapon:
    def __init__(self, dict_of_weapon: dict) -> None:
        self.name: str = dict_of_weapon.get("name").title()
        self.power = dict_of_weapon.get("power")


class Potion:
    def __init__(self, dict_of_potion: dict) -> None:
        self.name = dict_of_potion.get("name").title()

        if dict_of_potion.get("effect"):
            dict_of_potion = dict_of_potion.get("effect")

        self.hp = dict_of_potion.get("hp", 0)
        self.power = dict_of_potion.get("power", 0)
        self.protection = dict_of_potion.get("protection", 0)
