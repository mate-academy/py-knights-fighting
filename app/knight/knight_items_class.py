class Armour:
    def __init__(self, dict_of_armour: dict) -> None:
        self.part: str = dict_of_armour.get("part").title()
        self.protection: int = dict_of_armour.get("protection")


class Weapon:
    def __init__(self, dict_of_weapon: dict) -> None:
        self.name: str = dict_of_weapon.get("name").title()
        self.power: int = dict_of_weapon.get("power")


class Potion:
    def __init__(self, dict_of_potion: dict) -> None:
        self.name: str = dict_of_potion.get("name").title()

        effect = None
        if dict_of_potion.get("effect"):
            effect = dict_of_potion.get("effect")

        self.hp: int = effect.get("hp", 0)
        self.power: int = effect.get("power", 0)
        self.protection: int = effect.get("protection", 0)
