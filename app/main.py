class Knight:

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: list,
            weapon: dict,
            potion: dict
    ) -> None:
        self.protection = 0
        self.name = name
        self.power = power
        self.hp = hp
        self.armour = armour
        self.weapon = weapon
        self.potion = potion

    def take_weapon(self) -> None:
        self.power += self.weapon["power"]

    def put_on_armor(self) -> None:
        for armor in self.armour:
            self.protection += armor["protection"]

    def use_potion(self) -> None:
        if self.potion:
            potion_effect = self.potion["effect"]
            for key, value in potion_effect.items():
                if hasattr(self, key):
                    current_value = getattr(self, key)
                    setattr(self, key, current_value + value)

    def get_ready_to_battle(self) -> None:
        self.take_weapon()
        self.put_on_armor()
        self.use_potion()


class BattleArena:

    @staticmethod
    def check_hp(warriors: list) -> None:
        for warrior in warriors:
            if warrior.hp <= 0:
                print(f"{warrior.name} was defeated!")
                warrior.hp = 0

    @staticmethod
    def fight(warriors: list) -> dict:
        for warrior in warriors:
            warrior.get_ready_to_battle()

        warriors[0].hp -= warriors[2].power - warriors[0].protection
        warriors[2].hp -= warriors[0].power - warriors[2].protection
        warriors[1].hp -= warriors[3].power - warriors[1].protection
        warriors[3].hp -= warriors[1].power - warriors[3].protection

        BattleArena.check_hp(warriors)

        return {
            warriors[0].name: warriors[0].hp,
            warriors[1].name: warriors[1].hp,
            warriors[2].name: warriors[2].hp,
            warriors[3].name: warriors[3].hp,
        }


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
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
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
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
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
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


def battle(config_knigths: dict) -> dict:
    warriors = [
        Knight(
            warrior["name"],
            warrior["power"],
            warrior["hp"],
            warrior["armour"],
            warrior["weapon"],
            warrior["potion"]
        )
        for warrior in config_knigths.values()
    ]
    return BattleArena.fight(warriors)
