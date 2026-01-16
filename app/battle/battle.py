from app.battle.battle_preparation import battle_preparation
from app.knights.knight import Knight


def apply_damage(knight1: Knight, knight2: Knight) -> tuple:
    damage_knight1 = knight2.power - knight1.protection
    damage_knight2 = knight1.power - knight2.protection

    knight1.decrease_hp(damage_knight1)
    knight2.decrease_hp(damage_knight2)

    return knight1, knight2


def battle(knights_config: dict) -> dict:
    prepared_knights = battle_preparation(knights_config)

    lancelot, mordred = apply_damage(
        prepared_knights["lancelot"],
        prepared_knights["mordred"]
    )
    arthur, red_knight = apply_damage(
        prepared_knights["arthur"],
        prepared_knights["red_knight"]
    )

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp
    }
