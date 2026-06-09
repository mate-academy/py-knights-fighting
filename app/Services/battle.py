from app.Objects.knight import Knight


def battle(knights: dict[str, Knight]) -> dict[str, int]:

    lancelot = knights["lancelot"]
    mordred = knights["mordred"]
    arthur = knights["arthur"]
    red_knight = knights["red_knight"]

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        mordred.name: mordred.hp,
        arthur.name: arthur.hp,
        red_knight.name: red_knight.hp,
    }


def fight(knight1: Knight, knight2: Knight) -> None:
    knight2.get_damage(knight1)

    knight1.get_damage(knight2)
