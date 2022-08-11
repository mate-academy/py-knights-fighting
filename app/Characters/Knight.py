class Knight:
    knights = dict()

    def __init__(self, name: str, power: int, hp: int):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0
        self.__class__.knights[name] = self

    @staticmethod
    def knight_from_dict(knight_dict: dict):
        knight = Knight(knight_dict["name"],
                        knight_dict["power"],
                        knight_dict["hp"])
        knight.add_protection_from_armor(knight_dict)
        knight.add_power_from_weapon(knight_dict)
        if knight_dict["potion"] is not None:
            stats = ("protection", "power", "hp")
            effect = knight_dict["potion"]["effect"]
            for stat in stats:
                if stat in effect:
                    knight.__setattr__(
                        stat,
                        knight.__getattribute__(stat) + effect[stat])
        return knight

    def add_protection_from_armor(self, armor_list):
        for armour in armor_list["armour"]:
            self.protection += armour["protection"]

    def add_power_from_weapon(self, weapon_data):
        self.power += weapon_data["weapon"]["power"]

    def change_knights_hp(self, other):
        self.hp -= min(self.hp, other.power - self.protection)
        other.hp -= min(other.hp, self.power - other.protection)
