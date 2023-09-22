from app.knights import Knight, lancelot, mordred, arthur, red_knight


def battle(knight1: Knight, knight2: Knight) -> dict:
    knight1.apply_armor()
    knight1.apply_potion()
    knight2.apply_armor()
    knight2.apply_potion()

    knight1.attack(knight2)
    knight2.attack(knight1)

    if knight1.hp <= 0:
        knight1.hp = 0
    if knight2.hp <= 0:
        knight2.hp = 0

    return {
        knight1.name: knight1.hp,
        knight2.name: knight2.hp
    }


# Perform battles
battle_result_1 = battle(lancelot, mordred)
battle_result_2 = battle(arthur, red_knight)

print("Battle Result 1:", battle_result_1)
print("Battle Result 2:", battle_result_2)
