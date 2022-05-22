class Knight:
    def __init__(self, name, power, hp, protection):
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = protection

    @classmethod
    def create_knight(cls, data):
        name = data["name"]
        power = sum(
            [
                data["power"],
                cls.get_potion_points(data["potion"], "power"),
                data["weapon"]["power"]
            ]
        )
        hp = sum(
            [
                data["hp"],
                cls.get_potion_points(data["potion"], "hp")
            ]
        )
        protection = sum(
            [
                cls.get_armour_points(data["armour"]),
                cls.get_potion_points(data["potion"], "protection")
            ]
        )

        return cls(name, power, hp, protection)

    @staticmethod
    def get_armour_points(armour_data):
        if not armour_data:
            return 0
        points = 0
        for element in armour_data:
            points += element["protection"]

        return points

    @staticmethod
    def get_potion_points(potion_data, stat):
        if not potion_data:
            return 0
        if stat in potion_data["effect"]:
            return potion_data["effect"][stat]
        else:
            return 0

    def __isub__(self, other):
        self.hp -= other.power - self.protection
        if self.hp < 0:
            self.hp = 0

        return self
