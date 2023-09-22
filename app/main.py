
KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {"name": "Metal Sword", "power": 50,},
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
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
            }
        ],
        "weapon": {"name": "Two-handed Sword", "power": 55,},
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {"name": "Poisoned Sword", "power": 60,},
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
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


class Tournament:

    def __init__(self):
        self.knights_list = []
        self.results = None


    def create_battle_pairs(self):
        pairs = []
        for i in range(0, len(self.knights_list)//2):
            pairs.append(
                (self.knights_list[i], self.knights_list[i + 2])
            )
        return pairs


    def battle(self, knight):
        knight[0].hp -= knight[1].power - knight[0].protection
        if knight[0].hp <= 0:
            knight[0].hp = 0

        knight[1].hp -= knight[0].power - knight[1].protection
        if knight[1].hp <= 0:
            knight[1].hp = 0

    def results_of_tournament(self):
        result = {}
        for knight in self.create_battle_pairs():
            self.battle(knight)
            result[knight[0].name] = knight[0].hp
            result[knight[1].name] = knight[1].hp


    class Knight:

        def __init__(
                self,
                name: str,
                power: float,
                hp: float,
                armour: list,
                weapon: dict,
                potion: dict
            ) -> None:
            self.name = name
            self.power = power
            self.hp = hp
            self.armour = armour
            self.weapon = weapon
            self.potion = potion
            self.protection = 0
            tournament.knights_list.append(self)


        def apply_armour(self):
            for armour in self.armour:
                self.protection += armour["protection"]


        def apply_potion(self):
            if self.potion:
                if "hp" in self.potion["effect"].keys():
                    self.hp += self.potion["effect"]["hp"]

                if "power" in self.potion["effect"].keys():
                    self.power += self.potion["effect"]["power"]

                if "protection" in self.potion["effect"].keys():
                    self.protection += self.potion["effect"]["protection"]


        def prepare_knight(self):
            self.apply_armour()
            self.apply_potion()


tournament = Tournament()

lancelot_knight = Tournament.Knight(
    list(KNIGHTS.keys())[0],
    KNIGHTS[list(KNIGHTS.keys())[0]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[0]]["potion"]
)
arthur_knight = Tournament.Knight(
        list(KNIGHTS.keys())[1],
    KNIGHTS[list(KNIGHTS.keys())[1]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[1]]["potion"]
)
mordred_knight = Tournament.Knight(
        list(KNIGHTS.keys())[2],
    KNIGHTS[list(KNIGHTS.keys())[2]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[2]]["potion"]
)
red_knight = Tournament.Knight(
        list(KNIGHTS.keys())[3],
    KNIGHTS[list(KNIGHTS.keys())[3]]["power"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["hp"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["armour"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["weapon"],
    KNIGHTS[list(KNIGHTS.keys())[3]]["potion"]
)



tournament.results_of_tournament()
