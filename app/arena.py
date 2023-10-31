from app.knight import Knight


def battle(all_knights: dict) -> dict:
    for sir in all_knights.values():
        Knight(sir["name"],
               sir["power"],
               sir["hp"],
               sir["armour"],
               sir["weapon"],
               sir["potion"])

    Knight.fight(
        Knight.dict_knights["Lancelot"],
        Knight.dict_knights["Mordred"])

    Knight.fight(
        Knight.dict_knights["Arthur"],
        Knight.dict_knights["Red Knight"])

    return {
        knight.name: knight.hp
        for knight in Knight.dict_knights.values()}
