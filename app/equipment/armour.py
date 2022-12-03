from app.keys import KeysArmour


class Armour:
    def __init__(self, list_armour: list) -> None:
        sum_protect = 0
        for dictionary in list_armour:
            self.part = dictionary[KeysArmour.PART.value]
            self.protection = dictionary[KeysArmour.PROTECTION.value]
            sum_protect += self.protection
        self.sum_protect = sum_protect
