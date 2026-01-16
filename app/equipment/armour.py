from app.keys import KeysArmour


class Armour:
    def __init__(self, list_armour: list) -> None:
        protect = []
        for dictionary in list_armour:
            self.part = dictionary[KeysArmour.PART.value]
            self.protection = dictionary[KeysArmour.PROTECTION.value]
            protect.append(self.protection)
        self.sum_protect = sum(protect)
