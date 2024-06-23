from app.knight import Knight


def prepare_knight(knight_data: dict) -> Knight:
    knight = Knight(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        armour=knight_data["armour"],
        weapon=knight_data["weapon"],
        potion=knight_data["potion"],
    )
    knight.prepare_for_battle()
    return knight


def engage_battle(knight1: Knight, knight2: Knight) -> None:
    knight1.take_damage(knight2.power - knight1.protection)
    knight2.take_damage(knight1.power - knight2.protection)


def battle(knights: dict) -> dict:
    lancelot = prepare_knight(knights["lancelot"])
    arthur = prepare_knight(knights["arthur"])
    mordred = prepare_knight(knights["mordred"])
    red_knight = prepare_knight(knights["red_knight"])

    engage_battle(lancelot, mordred)
    engage_battle(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
