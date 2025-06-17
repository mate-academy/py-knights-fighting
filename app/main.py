from app.knights.knight_inst import Knight

KNIGHTS = {
    "lancelot": Knight(
        name="Lancelot",
        power=35,
        hp=100,
        armour=[],
        weapon={
            "name": "Metal Sword",
            "power": 50,
        },
        potion=None,
    ),
    "arthur": Knight(
        name="Arthur",
        power=45,
        hp=75,
        armour=[
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
        weapon={
            "name": "Two-handed Sword",
            "power": 55,
        },
        potion=None,
    ),
    "mordred": Knight(
        name="Mordred",
        power=30,
        hp=90,
        armour=[
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        weapon={
            "name": "Poisoned Sword",
            "power": 60,
        },
        potion={
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    ),
    "red_knight": Knight(
        name="Red Knight",
        power=40,
        hp=70,
        armour=[
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        weapon={
            "name": "Sword",
            "power": 45
        },
        potion={
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    )
}


def battle(knights_config: dict) -> dict:
    lancelot_obj = knights_config["lancelot"]
    arthur_obj = knights_config["arthur"]
    mordred_obj = knights_config["mordred"]
    red_knight_obj = knights_config["red_knight"]

    lancelot_obj.prepare_for_battle()
    arthur_obj.prepare_for_battle()
    mordred_obj.prepare_for_battle()
    red_knight_obj.prepare_for_battle()

    lancelot_obj.take_damage(mordred_obj.current_power)
    mordred_obj.take_damage(lancelot_obj.current_power)

    arthur_obj.take_damage(red_knight_obj.current_power)
    red_knight_obj.take_damage(arthur_obj.current_power)
    return {arthur_obj.name: arthur_obj.current_hp,
            lancelot_obj.name: lancelot_obj.current_hp,
            mordred_obj.name: mordred_obj.current_hp,
            red_knight_obj.name: red_knight_obj.current_hp
            }


print(battle(KNIGHTS))
