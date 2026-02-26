from app.knight import Knight


def perform_battle(knight1: Knight,
                   knight2: Knight) -> dict:
    knight1_hp = (knight1.hp
                  - (knight2.power
                     - knight1.protection))
    knight2_hp = (knight2.hp
                  - (knight1.power
                     - knight2.protection))

    return {
        knight1.name: 0 if knight1_hp <= 0 else knight1_hp,
        knight2.name: 0 if knight2_hp <= 0 else knight2_hp,
    }
