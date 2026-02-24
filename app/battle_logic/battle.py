from app.solution.knights import Knight


def fight(knight_one: Knight, knight_two: Knight) -> None:
    knight_one.hp -= max(0, knight_two.power - knight_one.protection)
    knight_two.hp -= max(0, knight_one.power - knight_two.protection)
    knight_one.hp = max(0, knight_one.hp)
    knight_two.hp = max(0, knight_two.hp)


def battle(knights_config: dict[str, dict]) -> dict:
    knights = {key: Knight.from_dict(cfg).prepare_stats()
               for key, cfg in knights_config.items()}

    lancelot, mordred = knights["lancelot"], knights["mordred"]
    arthur, red_knight = knights["arthur"], knights["red_knight"]

    fight(lancelot, mordred)
    fight(arthur, red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
