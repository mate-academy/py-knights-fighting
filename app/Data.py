class KNIGHTS:

    KNIGHTS = {}

    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.KNIGHTS.update({self.name: {
            "name": self.name.title().replace("_", " "),
            "power": self.power,
            "hp": self.hp,
            "armour": [],
            "weapon": {},
            "potion": None}})

    def add_armour(self, part: str, protection: int) -> None:
        self.KNIGHTS[self.name]["armour"].append({"part": part,
                                                  "protection": protection})

    def add_weapon(self, name: str, power: int) -> None:
        self.KNIGHTS[self.name]["weapon"] = {"name": name, "power": power}

    def add_potion(self,
                   name: str,
                   hp: int = 0,
                   power: int = 0,
                   protection: int = 0) -> None:
        self.KNIGHTS[self.name]["potion"] = {"name": name, "effect" : {}}
        if hp:
            self.KNIGHTS[self.name]["potion"]["effect"]["power"] = power
        if power:
            self.KNIGHTS[self.name]["potion"]["effect"]["hp"] = hp
        if protection:
            self.KNIGHTS[self.name]["potion"]["effect"]["protection"] = (
                protection)


lancelot = KNIGHTS("lancelot", 35, 100)
lancelot.add_weapon("Metal Sword", 50)

arthur = KNIGHTS("arthur", 45, 75)
arthur.add_armour("helmet", 15)
arthur.add_armour("breastplate", 20)
arthur.add_armour("boots", 10)
arthur.add_weapon("Two-handed Sword", 55)

mordred = KNIGHTS("mordred", 30, 90)
mordred.add_armour("breastplate", 15)
mordred.add_armour("boots", 10)
mordred.add_weapon("Poisoned Sword", 60)
mordred.add_potion("Berserk", power=+15, hp=-5, protection=+10)

red_knight = KNIGHTS("red_knight", 40, 70)
red_knight.add_armour("breastplate", 15)
red_knight.add_weapon("Sword", 45)
red_knight.add_potion("Blessing", hp=-5, power=+5)
