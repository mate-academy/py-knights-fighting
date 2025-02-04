from app.knights.knight import Knight
from app.items.gear_set import GearSet


def summon_knights() -> list[Knight]:
    knights = [Knight("Lancelot", 35, 100),
               Knight("Arthur", 45, 75),
               Knight("Mordred", 30, 90),
               Knight("Red Knight", 40, 70)]

    gear_set = GearSet.prepare_gear_for_knights()
    for knight in knights:
        knight.suit_up(gear_set[knight.name])


def round_turn(knight1: Knight, knight2: Knight) -> Knight:
    knight1.strike(knight2)
    knight2.strike(knight1)
    if knight1.is_defeated():
        return knight2
    elif knight2.is_defeated():
        return knight1
    else:
        return None


def battle_round(knight1: Knight, knight2: Knight) -> Knight:
    victor = None
    while victor is None:
        victor = battle_round(knight1, knight2)

    print(f"{victor.name} defeated the opponent.")
    return victor


def battle(knights: list[Knight]) -> None:
    round_1_victor1 = battle_round(knights[0], knights[1])
    round_1_victor2 = battle_round(knights[2], knights[3])
    tournament_victor = battle_round(round_1_victor1, round_1_victor2)
    print(f"{tournament_victor.name} has won the tournament.")
