class Knight:
    knights = dict()

    def __init__(self, name: str, power: int, hp: int):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.__class__.knights[name] = self

    @staticmethod
    def knight_from_dict(val: dict):
        knight = Knight(val["name"], val["power"], val["hp"])
        knight.add_protection_from_armor(val)
        knight.add_power_from_weapon(val)
        if val["potion"] is not None:
            if "power" in val["potion"]["effect"]:
                knight.power += val["potion"]["effect"]["power"]

            if "protection" in val["potion"]["effect"]:
                knight.protection += val["potion"]["effect"]["protection"]

            if "hp" in val["potion"]["effect"]:
                knight.hp += val["potion"]["effect"]["hp"]
        return knight

    def add_protection_from_armor(self, val):
        for armour in val["armour"]:
            self.protection += armour["protection"]

    def add_power_from_weapon(self, val):
        self.power += val["weapon"]["power"]

    def change_knights_hp(self, other):
        self.hp -= min(self.hp, other.power - self.protection)
        other.hp -= min(other.hp, self.power - other.protection)
