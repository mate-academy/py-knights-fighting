def perform_battle(knight1, knight2):
    knight1.apply_armour()
    knight1.apply_weapon()
    knight1.apply_potion()

    knight2.apply_armour()
    knight2.apply_weapon()
    knight2.apply_potion()

    knight1_hp = knight1.hp - (knight2.power - knight1.protection)
    knight2_hp = knight2.hp - (knight1.power - knight2.protection)

    if knight1_hp <= 0:
        knight1_hp = 0
    if knight2_hp <= 0:
        knight2_hp = 0

    return {
        knight1.name: knight1_hp,
        knight2.name: knight2_hp,
    }
