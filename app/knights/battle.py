from app.knights.utils import calculate_knight_stats


def battle_between(knight1: dict, knight2: dict) -> tuple:
    knight1_power, knight1_hp, knight1_protection \
        = calculate_knight_stats(knight1)
    knight2_power, knight2_hp, knight2_protection\
        = calculate_knight_stats(knight2)

    knight1_hp -= knight2_power - knight1_protection
    knight2_hp -= knight1_power - knight2_protection

    knight1_hp = max(knight1_hp, 0)
    knight2_hp = max(knight2_hp, 0)

    return knight1_hp, knight2_hp


def battle(knights_config: dict) -> dict:
    knights = ["lancelot", "mordred", "arthur", "red_knight"]
    results = {}

    for i in range(0, len(knights), 2):
        knight1, knight2 = knights[i], knights[i + 1]
        knight1_hp, knight2_hp = (
            battle_between(knights_config[knight1], knights_config[knight2]))

        results[knights_config[knight1]["name"]] = knight1_hp
        results[knights_config[knight2]["name"]] = knight2_hp

    return results
