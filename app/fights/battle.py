from app.knights.knight import Knight


def battle(knights: dict) -> dict:
    knights_objects = {name: Knight(**data)
                       for name, data in knights.items()}
    matchups = [
        ("lancelot", "mordred"),
        ("arthur", "red_knight"),
    ]

    for knight1_name, knight2_name in matchups:
        knight1 = knights_objects[knight1_name]
        knight2 = knights_objects[knight2_name]

        knight1.attack(knight2)
        knight2.attack(knight1)

    results = {knight.name: max(knight.hp, 0)
               for knight in knights_objects.values()}
    return results
