from app.extraction.extraction_first_dict import extract_first_dict

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


class Knight:
    def __init__(self, knight_data: dict) -> None:
        self.knight_data = knight_data
        self.name = ""
        self.total_hp = 0
        self.total_power = 0
        self.total_protection = 0
        self._initialize_stats()

    def _initialize_stats(self) -> None:
        first_dict = extract_first_dict(self.knight_data)
        key, data = next(iter(first_dict.items()))
        self.name = data.get("name", key)

        base_hp = data.get("hp", 0)
        base_power = data.get("power", 0)
        weapon_power = data.get("weapon", {}).get("power", 0)
        armour_list = data.get("armour", [])
        total_protection = sum(a.get("protection", 0) for a in armour_list)

        potion = data.get("potion")
        potion_hp = potion.get("effect", {}).get("hp", 0) if potion else 0
        potion_power = potion.get("effect", {}).get("power", 0) \
            if potion else 0
        potion_protection = potion.get("effect", {}).get("protection", 0) \
            if potion else 0

        self.total_hp = base_hp + potion_hp
        self.total_power = base_power + weapon_power + potion_power
        self.total_protection = total_protection + potion_protection

    def take_damage(self, damage: int) -> None:
        self.total_hp = max(0, self.total_hp - damage)


def battle(knights_config: dict) -> dict:
    lancelot = Knight({"lancelot": knights_config["lancelot"]})
    arthur = Knight({"arthur": knights_config["arthur"]})
    mordred = Knight({"mordred": knights_config["mordred"]})
    red_knight = Knight({"red_knight": knights_config["red_knight"]})

    mordred_damage = max(0, lancelot.total_power - mordred.total_protection)
    lancelot_damage = max(0, mordred.total_power - lancelot.total_protection)
    lancelot.take_damage(lancelot_damage)
    mordred.take_damage(mordred_damage)

    red_knight_damage = max(0, arthur.total_power
                            - red_knight.total_protection)
    arthur_damage = max(0, red_knight.total_power
                        - arthur.total_protection)
    arthur.take_damage(arthur_damage)
    red_knight.take_damage(red_knight_damage)

    return {
        lancelot.name: lancelot.total_hp,
        arthur.name: arthur.total_hp,
        mordred.name: mordred.total_hp,
        red_knight.name: red_knight.total_hp,
    }
