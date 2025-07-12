from app.knights.create_knight import Knight

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


def battle(knights_config: dict) -> dict:
    for name_knight in knights_config:
        knight_info = knights_config[name_knight]
        Knight(
            name=knight_info["name"],
            power=knight_info["power"],
            hp=knight_info["hp"],
            armour=knight_info["armour"],
            weapon=knight_info["weapon"],
            potion=knight_info["potion"]
        )

    for lancelot in Knight.knights:
        if lancelot.name == "Lancelot":
            for mordred in Knight.knights:
                if mordred.name == "Mordred":
                    lancelot_hp_after_battle = (
                        lancelot.calculate_hp()
                        - (
                            mordred.calculate_power()
                            - lancelot.calculate_armour()
                        )
                    )
                    if lancelot_hp_after_battle < 0:
                        lancelot_hp_after_battle = 0
                    mordred_hp_after_battle = (
                        mordred.calculate_hp()
                        - (
                            lancelot.calculate_power()
                            - mordred.calculate_armour()
                        )
                    )
                    if mordred_hp_after_battle < 0:
                        mordred_hp_after_battle = 0

    for arthur in Knight.knights:
        if arthur.name == "Arthur":
            for red_knight in Knight.knights:
                if red_knight.name == "Red Knight":
                    arthur_hp_after_battle = (
                        arthur.calculate_hp()
                        - (
                            red_knight.calculate_power()
                            - arthur.calculate_armour()
                        )
                    )
                    if arthur_hp_after_battle < 0:
                        arthur_hp_after_battle = 0
                    red_knight_hp_after_battle = (
                        red_knight.calculate_hp()
                        - (
                            arthur.calculate_power()
                            - red_knight.calculate_armour()
                        )
                    )
                    if red_knight_hp_after_battle < 0:
                        red_knight_hp_after_battle = 0
    return {
        "Lancelot": lancelot_hp_after_battle,
        "Arthur": arthur_hp_after_battle,
        "Mordred": mordred_hp_after_battle,
        "Red Knight": red_knight_hp_after_battle
    }


print(battle(KNIGHTS))
