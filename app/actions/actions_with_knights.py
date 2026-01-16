from app.characters.knight import Knight


def check_knight_hp(knight: Knight) -> None:
    if knight.hp <= 0:
        knight.hp = 0


def combat_action(first: Knight, second: Knight) -> None:
    first.hp -= second.power - first.protection
    second.hp -= first.power - second.protection


def fight_between_knights(first: Knight, second: Knight) -> dict:
    first.prepare_for_battle()
    second.prepare_for_battle()
    combat_action(first, second)
    check_knight_hp(first)
    check_knight_hp(second)
    return {first.name: first.hp, second.name: second.hp}
