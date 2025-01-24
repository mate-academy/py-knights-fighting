class Knight:
    def __init__(self, name, power, hp, armour, weapon, potion=None):
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def get_total_protection(self):
        return sum(item['protection'] for item in self.armour)

    def apply_potion(self):
        if self.potion:
            if 'power' in self.potion['effect']:
                self.power += self.potion['effect']['power']
            if 'hp' in self.potion['effect']:
                self.hp += self.potion['effect']['hp']
            if 'protection' in self.potion['effect']:
                for item in self.armour:
                    item['protection'] += self.potion['effect']['protection']

    def attack(self, opponent):
        total_power = self.power + self.weapon['power']
        total_protection = opponent.get_total_protection()

        damage = max(0, total_power - total_protection)
        opponent.hp -= damage
        return damage

    def __repr__(self):
        return f"{self.name} (HP: {self.hp}, Power: {self.power})"


lancelot = Knight(
    name="Lancelot",
    power=35,
    hp=100,
    armour=[],
    weapon={"name": "Metal Sword", "power": 50},
    potion=None
)

arthur = Knight(
    name="Arthur",
    power=45,
    hp=75,
    armour=[
        {"part": "helmet", "protection": 15},
        {"part": "breastplate", "protection": 20},
        {"part": "boots", "protection": 10}
    ],
    weapon={"name": "Two-handed Sword", "power": 55},
    potion=None
)

mordred = Knight(
    name="Mordred",
    power=30,
    hp=90,
    armour=[
        {"part": "breastplate", "protection": 15},
        {"part": "boots", "protection": 10}
    ],
    weapon={"name": "Poisoned Sword", "power": 60},
    potion={
        "name": "Berserk",
        "effect": {
            "power": 15,
            "hp": -5,
            "protection": 10
        }
    }
)

red_knight = Knight(
    name="Red Knight",
    power=40,
    hp=70,
    armour=[
        {"part": "breastplate", "protection": 25}
    ],
    weapon={"name": "Sword", "power": 45},
    potion={
        "name": "Blessing",
        "effect": {
            "hp": 10,
            "power": 5
        }
    }
)

lancelot.attack(arthur)
