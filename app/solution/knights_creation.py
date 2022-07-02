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
            for armour in knight["armour"]:
                knight["protection"] += armour["protection"]
            knight["power"] += knight["weapon"]["power"]
            if knight["potion"] is not None:
                stats = ["protection", "power", "hp"]
                for stat in stats:
                    if stat in knight["potion"]["effect"]:
                        knight[stat] += knight["potion"]["effect"][stat]
            new_dict.update({name: Knights(knight["name"],
                                           knight["power"],
                                           knight["hp"],
                                           knight["protection"])})
        return new_dict

    def one_battle(self, other):
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
