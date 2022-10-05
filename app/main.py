from app.knight.knight import Knight


def battle(knights: dict) -> dict:
    knights = Knight.convert(knights)

    Knight.battle_between(knights["lancelot"], knights["mordred"])
    Knight.battle_between(knights["arthur"], knights["red_knight"])
    return {
        knight.name: knight.health
        for knight in knights.values()
    }
