from app.knights.knight import Knight


def knight_initialization(knight: dict) -> Knight:

    knight_obj = Knight(
        knight["name"],
        knight["power"],
        knight["hp"],
        knight["armour"],
        knight["weapon"],
        knight["potion"]
    )

    knight_obj.armour_protection()
    knight_obj.apply_weapon()
    knight_obj.apply_potion_if_exist()

    return knight_obj


def knight_battle(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.battle(knight_2)
    knight_2.battle(knight_1)

    knight_1.check_fell()
    knight_2.check_fell()
