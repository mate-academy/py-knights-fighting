from app.knights.knight import Knight


def perform_battle(knight1: Knight, knight2: Knight) -> dict:
    knights = (knight1, knight2)
    for knight in knights:
        knight.apply_armour()
        knight.apply_weapon()
        knight.apply_potion()

    knight1_hp = knight1.hp - (knight2.power - knight1.protection)
    knight2_hp = knight2.hp - (knight1.power - knight2.protection)

    knight1_hp = max(0, knight1_hp)
    knight2_hp = max(0, knight2_hp)

    return {
        knight1.name: knight1_hp,
        knight2.name: knight2_hp,
    }
