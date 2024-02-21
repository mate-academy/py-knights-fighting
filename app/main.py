from app.knights.knight import create_knight, fight


def battle(knights_config: dict) -> dict:
    arthur = create_knight(knights_config, "arthur")
    mordred = create_knight(knights_config, "mordred")
    lancelot = create_knight(knights_config, "lancelot")
    red_knight = create_knight(knights_config, "red_knight")

    fight1 = fight(lancelot, mordred)
    fight2 = fight(arthur, red_knight)

    fight1.update(fight2)

    return fight1
