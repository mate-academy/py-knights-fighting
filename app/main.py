from app.knights.knight import Knight


def battle(knight_config: dict) -> dict:

    # create new king from Class Knight
    knight_list = {}

    for knight_name, knight_value in knight_config.items():
        knight_list[knight_name] = Knight(knight_value)
    #
    # lancelot = Knight(knight_config["lancelot"])
    # arthur = Knight(knight_config["arthur"])
    # mordred = Knight(knight_config["mordred"])
    # red_knight = Knight(knight_config["red_knight"])

    # battle Lancelot vs Mordred
    apply_battle_result(knight_list["lancelot"], knight_list["mordred"])
    # Arthur vs Red Knight
    apply_battle_result(knight_list["arthur"], knight_list["red_knight"])

    return {knight.name: knight.hp for knight in knight_list.values()}


def apply_battle_result(hero1: Knight, hero2: Knight) -> None:
    dmg_to_hero1 = max(0, hero2.power - hero1.protection)
    dmg_to_hero2 = max(0, hero1.power - hero2.protection)

    hero1.take_damage(dmg_to_hero1)
    hero2.take_damage(dmg_to_hero2)

    if hero1.hp < 0:
        hero1.hp = 0
    if hero2.hp < 0:
        hero2.hp = 0
