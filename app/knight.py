class Knight:
    def __init__(self,
                 name: str,
                 power: int,
                 hp: int,
                 armour: list,
                 weapon: dict,
                 potion: dict) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion


lancelot = Knight(
    "Lancelot",
    35,
    100,
    [],
    {
        "name": "Metal Sword",
        "power": 50,
    },
    None,
)

arthur = Knight(
    "Arthur",
    45,
    75,
    [
        {
            "part": "helmet",
            "protection": 15,
        },
        {
            "part": "breastplate",
            "protection": 20,
        },
        {
            "part": "boots",
            "protection": 10,
        },
    ],
    {
        "name": "Two-handed Sword",
        "power": 55,
    },
    None,
)

mordred = Knight(
    "Mordred",
    30,
    90,
    [
        {
            "part": "breastplate",
            "protection": 15,
        },
        {
            "part": "boots",
            "protection": 10,
        },
    ],
    {
        "name": "Poisoned Sword",
        "power": 60,
    },
    {
        "name": "Berserk",
        "effect": {
            "power": +15,
            "hp": -5,
            "protection": +10,
        },
    },
)

red_knight = Knight(
    "Red Knight",
    40,
    70,
    [
        {
            "part": "breastplate",
            "protection": 25,
        },
    ],
    {
        "name": "Sword",
        "power": 45,
    },
    {
        "name": "Blessing",
        "effect": {
            "hp": +10,
            "power": +5,
        },
    },
)

# transition obj to dict
lancelot = vars(lancelot)
arthur = vars(arthur)
mordred = vars(mordred)
red_knight = vars(red_knight)

KNIGHTS = {}

# add knights to KNIGHTS dict
# takes the value of the knight "name" and changes to to lowercase
KNIGHTS[lancelot["name"].lower()] = lancelot
KNIGHTS[arthur["name"].lower()] = arthur
KNIGHTS[mordred["name"].lower()] = mordred
KNIGHTS[red_knight["name"].lower().replace(" ", "_")] = red_knight
