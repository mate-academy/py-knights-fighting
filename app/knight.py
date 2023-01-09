class Knight:
    """Class creates the knight instance and necessary methods"""

    def __init__(self, name: str, knights: dict) -> None:
        """Method constructs knight instance"""
        self.name = name
        self.real_name = knights[name]["name"]
        self.power = knights[name]["power"]
        self.hp = knights[name]["hp"]
        self.armour = knights[name]["armour"]
        self.weapon = knights[name]["weapon"]
        self.potion = knights[name]["potion"]
        self.protection = 0

    def get_armour(self) -> None:
        """Method adds armour protection to the knight"""
        total_protection = 0
        for part in self.armour:
            total_protection += part["protection"]
        self.protection = total_protection

    def get_weapon(self) -> None:
        """Method adds the power of knight's weapon"""
        self.power += self.weapon["power"]

    def get_potion(self) -> None:
        """Method adds potion effect to the knight"""
        if self.potion is not None:
            skills = [self.power, self.hp, self.protection]
            for skill in skills:
                if skill in self.potion["effect"]:
                    skill += self.potion["effect"][skill]

    # def battle_preparation(self) -> None:
    #     self.get_armour()

#
# lancelot = Knight("lancelot", KNIGHTS)
# print(KNIGHTS["lancelot"]["weapon"]["name"])
# print(f"protection: {lancelot.protection}")
# print(f"power: {lancelot.power}")
# print(f"hp: {lancelot.hp}")
# lancelot.get_armour()
# lancelot.get_weapon()
# lancelot.get_potion()
# print("---------------")
# print(f"protection: {lancelot.protection}")
# print(f"power: {lancelot.power}")
# print(f"hp: {lancelot.hp}")
# print(lancelot.__dict__)
# mordred = Knight("mordred", KNIGHTS)
