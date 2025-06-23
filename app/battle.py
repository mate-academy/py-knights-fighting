from app.knights import Knight
import random


def attack_hits(attacker: Knight, defender: Knight) -> bool:
    # Ймовірність влучання = accuracy * (1 - evasion)
    return random.random() < attacker.accuracy * (1 - defender.evasion)


def battle(knight1: Knight, knight2: Knight) -> None:
    # knight1 атакує knight2
    if attack_hits(knight1, knight2):
        damage_to_2 = max(knight1.power - knight2.protection, 0)
    else:
        damage_to_2 = 0

    # knight2 атакує knight1
    if attack_hits(knight2, knight1):
        damage_to_1 = max(knight2.power - knight1.protection, 0)
    else:
        damage_to_1 = 0

    knight1.hp = max(knight1.hp - damage_to_1, 0)
    knight2.hp = max(knight2.hp - damage_to_2, 0)


def battle_round(
    lancelot: Knight,
    mordred: Knight,
    arthur: Knight,
    red_knight: Knight
) -> dict:
    battle(lancelot, mordred)
    battle(arthur, red_knight)
    return {
        lancelot.name: {
            "hp": lancelot.hp,
            "accuracy": lancelot.accuracy,
            "evasion": lancelot.evasion,
        },
        arthur.name: {
            "hp": arthur.hp,
            "accuracy": arthur.accuracy,
            "evasion": arthur.evasion,
        },
        mordred.name: {
            "hp": mordred.hp,
            "accuracy": mordred.accuracy,
            "evasion": mordred.evasion,
        },
        red_knight.name: {
            "hp": red_knight.hp,
            "accuracy": red_knight.accuracy,
            "evasion": red_knight.evasion,
        },
    }
