from app.knights.basic_stats import Knight


def fight(k1: Knight, k2: Knight) -> None:
    dmg1 = max(0, k2.power - k1.protection)
    dmg2 = max(0, k1.power - k2.protection)

    k1.hp = max(0, k1.hp - dmg1)
    k2.hp = max(0, k2.hp - dmg2)
