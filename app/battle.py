from app.knights.knight_class import Knight


def battle(knights: dict) -> dict:

    knight_objects = {
        knight["name"]: Knight(**knight) for knight in knights.values()
    }

    battles = [
        ("Lancelot", "Mordred"),
        ("Arthur", "Red Knight")
    ]

    for knight1, knight2 in battles:
        knight_objects[knight1].take_damage(knight_objects[knight2].power)
        knight_objects[knight2].take_damage(knight_objects[knight1].power)

    for knight in knight_objects.values():
        if knight.hp < 0:
            knight.hp = 0

    return {knight.name: knight.hp for knight in knight_objects.values()}
