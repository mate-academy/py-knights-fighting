from app.knights.knight import Knight
from app.knights.battle import fight


def battle(knights_config: dict) -> dict[str, int]:
    """Run two battles (Lancelot vs Mordred, Arthur vs Red Knight)
    and return their final HP."""

    knights_list = [
        Knight(
            name=k["name"],
            power=k["power"],
            hp=k["hp"],
            armour=k["armour"],
            weapon=k["weapon"],
            potion=k["potion"],
        )
        for k in knights_config.values()
    ]

    for knight in knights_list:
        knight.prepare()

    fight(knights_list[0], knights_list[2])
    fight(knights_list[1], knights_list[3])

    result = {knight.name: knight.hp for knight in knights_list}
    return result
