from app.knights import Knight


def knights_fight(knight1: Knight, knight2: Knight) -> dict:
    knight1.apply_potion()
    knight2.apply_potion()

    knight1_damage = max(
        0,
        knight1.damage() - knight2.armour.total_protection()
    )
    knight2_damage = max(
        0,
        knight2.damage() - knight1.armour.total_protection()
    )

    knight2.hp = max(0, knight2.hp - knight1_damage)
    knight1.hp = max(0, knight1.hp - knight2_damage)

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp,
    }
