class Knight:
    knights = []

    def __init__(self, name: str, power: int,
                 hp: int, armour: list, weapon: int,
                 potion):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

        self.knights.append(self)


lancelot = Knight(name="Lancelot", power=35, hp=100,
                  armour=[], weapon=50, potion=None)

arthur = Knight(name="Artur", power=45, hp=75,
                armour=[15, 20, 10], weapon=55, potion=None)

mordred = Knight(name="Mordred", power=30, hp=90,
                 armour=[15, 10], weapon=60,
                 potion={"name": "Berserk", "power": 15,
                         "hp": -5, "protection": 10})

red_knight = Knight(name="Red Knight", power=40, hp=70,
                    armour=[25], weapon=45,
                    potion={"name": "Blessing",
                            "hp": 10, "power": 5})
