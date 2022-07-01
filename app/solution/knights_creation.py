class Knights:

    def __init__(self, name, power, hp, protection):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @staticmethod
    def transformation(heroes: dict) -> dict:
        new_dict = {}
        for name, value in heroes.items():
            knight = heroes[name]
            knight["protection"] = 0
            for a in knight["armour"]:
                knight["protection"] += a["protection"]
            knight["power"] += knight["weapon"]["power"]
            if knight["potion"] is not None:
                if "power" in knight["potion"]["effect"]:
                    knight["power"] += knight["potion"]["effect"]["power"]
                if "protection" in knight["potion"]["effect"]:
                    knight["protection"] += \
                        knight["potion"]["effect"]["protection"]
                if "hp" in knight["potion"]["effect"]:
                    knight["hp"] += knight["potion"]["effect"]["hp"]
            new_dict.update({name: [knight["name"],
                                    knight["power"],
                                    knight["hp"],
                                    knight["protection"]]})
        return new_dict

    def one_battle(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
