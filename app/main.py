from app.knight import Knight


def battle(knights_config: dict) -> dict[str, int]:
    knights = create_knights(knights_config)
    for knight in knights:
        battle_preparations(knight)
    return start_battle(*knights)


def battle_preparations(knight: Knight) -> None:
    apply_armour(knight)
    apply_weapon(knight)
    use_potion(knight)


def start_battle(
        lancelot: Knight,
        arthur: Knight,
        mordred: Knight,
        red_knight: Knight
) -> dict[str, int]:
    # Lancelot vs Mordred
    duel_battle(lancelot, mordred)
    duel_battle(mordred, lancelot)

    # Arthur vs Red Knight
    duel_battle(arthur, red_knight)
    duel_battle(red_knight, arthur)

    return {
        knight.name: knight.hp
        for knight in [lancelot, arthur, mordred, red_knight]
    }


def create_knights(knights_config: dict) -> list:
    return [
        Knight(
            stats["name"],
            stats["power"],
            stats["hp"],
            armour=Knight.set_armours(stats["armour"]),
            weapon=Knight.set_weapon(stats["weapon"]),
            potion=Knight.set_potion(stats["potion"])
        )
        for stats in knights_config.values()
    ]


def duel_battle(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.hp = knight_1.hp - (knight_2.power - knight_1.protection)
    check_hp([knight_1, knight_2])


def check_hp(knights: list) -> None:
    for knight in knights:
        if knight.hp <= 0:
            knight.hp = 0


def apply_armour(knight: Knight) -> None:
    protection = 0
    if not knight.armour:
        knight.protection = protection
        return
    for armour in knight.armour:
        protection += armour.protection
    knight.protection = protection


def apply_weapon(knight: Knight) -> None:
    knight.power += knight.weapon.power


def use_potion(knight: Knight) -> None:
    knight.use_potion()


fords = {
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
            },
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
            },
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
            },
        },
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
        "weapon": {"name": "Sword", "power": 45},
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            },
        },
    },
}
kniggt = create_knights(fords)
for knigh in kniggt:
    battle_preparations(knigh)
    print(knigh)
print(battle(fords))
