class Knight:
    """Class makes the knight instances and necessary methods"""

    def __init__(self, name: str, knights: dict) -> None:
        """Method constructs knight instance"""
        self.name = knights.keys()
        self.power = knights[name]["power"]
        self.hp = knights[name]["hp"]
        self.protection = 0

    def get_armour(self, armour: list) -> None:
        """Method adds armour protection to the knight"""
        total_protection = 0
        for part in armour:
            total_protection += part["protection"]
        self.protection = total_protection

    def get_weapon(self, weapon: dict) -> None:
        """Method adds the power of knight's weapon"""
        self.power += weapon["power"]

    def get_potion(self, potion: dict | None) -> None:
        """Method adds potion effect to the knight"""
        if potion is not None:
            skills = [self.power, self.hp, self.protection]
            for skil in skills:
                if skil in potion["effect"]:
                    skil += potion["effect"][skil]
            # if "power" in potion["effect"]:
            #     self.power += potion["effect"]["power"]
            # if "hp" in potion["effect"]:
            #     self.hp += potion["effect"]["hp"]
            # if "protection" in potion["effect"]:
            #     self.protection += potion["effect"]["protection"]


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }

        }
    }
}

lancelot = Knight("lancelot", KNIGHTS)
print(KNIGHTS["lancelot"]["weapon"]["name"])
print(f"protection: {lancelot.protection}")
print(f"power: {lancelot.power}")
print(f"hp: {lancelot.hp}")
lancelot.get_armour(KNIGHTS["lancelot"]["armour"])
lancelot.get_weapon(KNIGHTS["lancelot"]["weapon"])
lancelot.get_potion(KNIGHTS["lancelot"]["potion"])
print("---------------")
print(f"protection: {lancelot.protection}")
print(f"power: {lancelot.power}")
print(f"hp: {lancelot.hp}")
