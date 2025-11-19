from app.accessories.armour import ArmourPiece
from app.accessories.potion import Potion
from app.accessories.weapon import Weapon
from app.knight import Knight


lancelot_weapon = Weapon("Metal Sword", 50)
lancelot = Knight("Lancelot", 35, 100,
                  [], lancelot_weapon, None)


arthur_helmet = ArmourPiece("helmet", 15)
arthur_breastplate = ArmourPiece("breastplate", 20)
arthur_boots = ArmourPiece("boots", 10)
arthur_weapon = Weapon("Two-handed Sword", 55)
arthur = Knight("Arthur",
                45, 75,
                [arthur_helmet, arthur_breastplate, arthur_boots],
                arthur_weapon, None)

mordred_breastplate = ArmourPiece("breastplate", 15)
mordred_boots = ArmourPiece("boots", 10)
mordred_weapon = Weapon("Poisoned Sword", 60)
mordred_potion = Potion("Berserk", {"power": 15, "hp": -5, "protection": 10})
mordred = Knight("Mordred",
                 30, 90,
                 [mordred_breastplate, mordred_boots],
                 mordred_weapon, mordred_potion)

red_knight_breastplate = ArmourPiece("breastplate", 25)
red_knight_weapon = Weapon("Sword", 45)
red_knight_potion = Potion("Blessing", {"power": 5, "hp": 10})
red_knight = Knight("Red Knight", 40, 70,
                    [red_knight_breastplate],
                    red_knight_weapon, red_knight_potion)

all_knights = [red_knight, lancelot, arthur, mordred]


def prepare_for_battle(knights: list) -> None:
    for knight in knights:
        knight.battle_preparation()


def duel(knight_1: Knight, knight_2: Knight) -> Knight | None:
    knight_1.battle(knight_2)
    knight_2.battle(knight_1)
    print(f"{knight_1.name} VS {knight_2.name}")
    if knight_1.hp > knight_2.hp:
        print(f"{knight_1.name} wins!"
              f"\n{knight_1.name}: {knight_1.hp}"
              f"\n{knight_2.name}: {knight_2.hp}")
        return knight_1
    if knight_1.hp < knight_2.hp:
        print(f"{knight_2.name} wins!"
              f"\n{knight_1.name}: {knight_1.hp}"
              f"\n{knight_2.name}: {knight_2.hp}")
        return knight_2
    else:
        print("Draw"
              f"\n{knight_1.name}: {knight_1.hp}"
              f"\n{knight_2.name}: {knight_2.hp}")
        return None


def tournament(knights: list) -> None:
    prepare_for_battle(knights)
    print("\n" + "=" * 40)
    print("THE KNIGHTS TOURNAMENT HAS BEGUN")
    print("=" * 40)
    print("\n--- SEMIFINAL 1 ---")
    winner_1 = duel(knights[0], knights[1])
    print("\n--- SEMIFINAL 2 ---")
    winner_2 = duel(knights[2], knights[3])
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
        the_best = duel(winner_1, winner_2)
        if the_best is None:
            print("Draw")
        else:
            print(f"{the_best.name} wins the tournament!")


tournament(all_knights)
