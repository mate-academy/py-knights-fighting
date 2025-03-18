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
    lancelot = knights_config["lancelot"]
    mordred = knights_config["mordred"]
    arthur = knights_config["arthur"]
    red_knight = knights_config["red_knight"]

    lancelot_hp, mordred_hp = battle_between(lancelot, mordred)

    arthur_hp, red_knight_hp = battle_between(arthur, red_knight)

    return {
        lancelot["name"]: lancelot_hp,
        arthur["name"]: arthur_hp,
        mordred["name"]: mordred_hp,
        red_knight["name"]: red_knight_hp,
    }
