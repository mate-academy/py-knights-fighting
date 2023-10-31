from app.knight import Knight


def battle(all_knights: dict) -> dict:
    for sir in all_knights:
        Knight(all_knights[sir]["name"],
               all_knights[sir]["power"],
               all_knights[sir]["hp"],
               all_knights[sir]["armour"],
               all_knights[sir]["weapon"],
               all_knights[sir]["potion"])

    Knight.fight(
        Knight.dict_knights["Lancelot"],
        Knight.dict_knights["Mordred"])

    Knight.fight(
        Knight.dict_knights["Arthur"],
        Knight.dict_knights["Red Knight"])

    return {
        knight: Knight.dict_knights[knight].hp
        for knight in Knight.dict_knights}
