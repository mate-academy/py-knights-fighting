from app.class_knight import Knight


def preparations_for_battle(knights_config: dict) -> list:
    make_knights2 = []
    for knight in knights_config.values():
        one_knight = Knight(knight["name"], knight)
        one_knight.config_preparations()
        make_knights2.append(one_knight)

    return make_knights2
