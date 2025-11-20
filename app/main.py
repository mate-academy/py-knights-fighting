from app.accessories.armour import ArmourPiece
from app.accessories.potion import Potion
from app.accessories.weapon import Weapon
from app.knight import Knight

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

all_knights = []
for knight_dict in KNIGHTS.values():
    knight_armour = []
    for armour in knight_dict["armour"]:
        knight_armour.append(ArmourPiece(**armour))
    knight_weapon = Weapon(knight_dict["weapon"]["name"],
                           knight_dict["weapon"]["power"])
    if knight_dict["potion"] is not None:
        knight_potion = Potion(knight_dict["potion"]["name"],
                               knight_dict["potion"]["effect"])
    else:
        knight_potion = None
    knight = Knight(knight_dict["name"],
                    knight_dict["power"],
                    knight_dict["hp"],
                    knight_armour,
                    knight_weapon,
                    knight_potion)
    all_knights.append(knight)


def prepare_for_battle(knights: list) -> None:
    for knight in knights:
        knight.battle_preparation()


def battle(knight_1: Knight, knight_2: Knight) -> Knight | None:
    print(f"{knight_1.name} VS {knight_2.name}")
    print("Before duel"
          f"\n{knight_1.name} has"
          f"\n{knight_1.power} power, "
          f"{knight_1.protection} protection, and "
          f"{knight_1.hp} hp.")
    print(f"{knight_2.name} has"
          f"\n{knight_2.power} power, "
          f"{knight_2.protection} protection, and "
          f"{knight_2.hp} hp.")
    knight_1.attack(knight_2)
    knight_2.attack(knight_1)
    if knight_1.hp > knight_2.hp:
        print(f"{knight_1.name} wins!"
              f"\n{knight_1.name}: {knight_1.hp} hp"
              f"\n{knight_2.name}: {knight_2.hp} hp")
        return knight_1
    if knight_1.hp < knight_2.hp:
        print(f"{knight_2.name} wins!"
              f"\n{knight_1.name}: {knight_1.hp} hp"
              f"\n{knight_2.name}: {knight_2.hp} hp")
        return knight_2
    else:
        print("Draw"
              f"\n{knight_1.name}: {knight_1.hp} hp"
              f"\n{knight_2.name}: {knight_2.hp} hp")
        return None


def tournament(knights: list) -> None:
    prepare_for_battle(knights)
    print("\n" + "=" * 40)
    print("THE KNIGHTS TOURNAMENT HAS BEGUN")
    print("=" * 40)
    print("\n--- SEMIFINAL 1 ---")
    winner_1 = battle(knights[0], knights[2])
    print("\n--- SEMIFINAL 2 ---")
    winner_2 = battle(knights[1], knights[3])
    print("\n" + "=" * 40)
    print("FINAL BATTLE HAS BEGUN")
    print("=" * 40)
    if winner_1 is None and winner_2 is None:
        print("Draw")
    elif winner_1 is None:
        print(f"{winner_2.name} wins!")
    elif winner_2 is None:
        print(f"{winner_1.name} wins!")
    else:
        print(f"--- FINAL: {winner_1.name} VS {winner_2.name} ---")
        winner_1.battle_preparation()
        winner_2.battle_preparation()
        the_best = battle(winner_1, winner_2)
        if the_best is None:
            pass
        else:
            print(f"{the_best.name} wins the tournament!")


tournament(all_knights)
