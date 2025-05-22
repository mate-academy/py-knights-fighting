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


class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.name = name
        self.power = power


class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.part = part
        self.protection = protection


class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.name = name
        self.effect = effect


class Knight:
    def __init__(self,
                 name: str,
                 base_power: int,
                 hp: int,
                 weapon: object,
                 armour: object = None,
                 potion: object = None
                 ) -> None:
        self.name = name
        self.base_power = base_power
        self.hp = hp
        self.weapon = weapon
        self.armour = armour if armour else []
        self.potion = potion
        self.power = base_power
        self.protection = 0
        self.prepare_for_battle()

    def prepare_for_battle(self) -> None:
        self.protection = sum(item.protection for item in self.armour)
        self.power += self.weapon.power
        if self.potion:
            effects = self.potion.effect
            self.power += effects.get("power", 0)
            self.protection += effects.get("protection", 0)
            self.hp += effects.get("hp", 0)

    def attack(self, enemy: object) -> None:
        damage = max(0, self.power - enemy.protection)
        enemy.hp -= damage
        if enemy.hp < 0:
            enemy.hp = 0


def battle(knights_dict: dict) -> dict:
    def create_knight(data: dict) -> Knight:
        armour = [Armour(**a) for a in data["armour"]]
        weapon = Weapon(**data["weapon"])
        potion = Potion(data["potion"]["name"],
                        data["potion"]["effect"]) if data["potion"] else None
        return Knight(data["name"],
                      data["power"],
                      data["hp"],
                      weapon,
                      armour,
                      potion)

    lancelot = create_knight(knights_dict["lancelot"])
    arthur = create_knight(knights_dict["arthur"])
    mordred = create_knight(knights_dict["mordred"])
    red_knight = create_knight(knights_dict["red_knight"])

    lancelot.attack(mordred)
    mordred.attack(lancelot)

    arthur.attack(red_knight)
    red_knight.attack(arthur)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp
    }


print(battle(KNIGHTS))
