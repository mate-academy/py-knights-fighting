from app.knights import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights.get("lancelot"))
    arthur = Knight(knights.get("arthur"))
    mordred = Knight(knights.get("mordred"))
    red_knight = Knight(knights.get("red_knight"))

    lancelot.exchange_shots(mordred)
    arthur.exchange_shots(red_knight)

    return lancelot.show_hp()
