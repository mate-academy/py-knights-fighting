def apply_preparation(knight_instances: dict) -> None:
    for knight_name, knight_instance in knight_instances.items():
        knight_instance.preparation()


def battle(knight_instances: dict) -> dict:
    lancelot = knight_instances["lancelot"]
    arthur = knight_instances["arthur"]
    mordred = knight_instances["mordred"]
    red_knight = knight_instances["red_knight"]

    lancelot.fight(mordred)
    arthur.fight(red_knight)

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
