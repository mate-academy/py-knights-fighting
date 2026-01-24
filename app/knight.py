class Knight():
    def __init__(self, knight_info: dict) -> None:
        self.name = knight_info["name"]
        self.power = knight_info["power"]
        self.hp = knight_info["hp"]
        self.armour = knight_info["armour"]
        self.weapon = knight_info["weapon"]
        self.potion = knight_info["potion"]

    def knights_stats(self):
        ammount_of_protection = 0
        if self.armour:
            for armor_part in self.armour:
                ammount_of_protection += armor_part["protection"]

        if not self.potion["effect"]["hp"]:
            ammount_of_hp = self.hp
        else:
            ammount_of_hp = self.hp + self.potion["effect"]["hp"]

        if not self.potion["effect"]["power"]:
            ammount_of_power = self.power + self.weapon["power"]
        else:
            ammount_of_power = self.power + self.weapon["power"] + self.potion["effect"]["power"]


        return {
            "hp": ammount_of_hp,  # 70 + 10
            "power": ammount_of_power,  # 40 + 45 + 5
            "protection": ammount_of_protection  # 0 + 25
        }


info = {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    }
x = Knight(info)
print(x.knights_stats())