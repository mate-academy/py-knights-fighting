from app.knight import Knight


# Setting up knights by creating Knight class
def set_up(knight: dict[list | str | int | dict]) -> Knight:
    single_knight = Knight(knight)
    return single_knight


# Fight between 2 knights
def duel(knight1: Knight, knight2: Knight) -> None:
    # taking damage realised by __sub__ method
    knight1 - knight2
    knight2 - knight1


def battle(all_knights: dict[list | str | int]) -> dict:
    lancelot = set_up(all_knights["lancelot"])
    arthur = set_up(all_knights["arthur"])
    mordred = set_up(all_knights["mordred"])
    red_knight = set_up(all_knights["red_knight"])

    # start fighting
    duel(lancelot, mordred)
    duel(arthur, red_knight)

    # returning result
    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
