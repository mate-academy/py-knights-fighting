from ..knights.knight_stats import Knight


def perform_battle(knight1, knight2):
    knight1.apply_armour()
    knight1.apply_potion()
    knight2.apply_armour()
    knight2.apply_potion()

    knight1.calculate_battle_result(knight2)
    knight2.calculate_battle_result(knight1)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }
