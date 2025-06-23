from app.knights import Knight


def battle(knight1: Knight, knight2: Knight) -> None:
    # knight1 атакує knight2
    damage_to_2 = max(knight1.power - knight2.protection, 0)
    # knight2 атакує knight1
    damage_to_1 = max(knight2.power - knight1.protection, 0)
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
        lancelot.name: {"hp": lancelot.hp},
        arthur.name: {"hp": arthur.hp},
        mordred.name: {"hp": mordred.hp},
        red_knight.name: {"hp": red_knight.hp},
    }
