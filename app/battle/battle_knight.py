from app.knights.knight import Knight


def knight_initialization(knight: dict) -> Knight:
    print(knight)
    knight["name"] = Knight(knight["name"], knight["power"],
                            knight["hp"], knight["armour"],
                            knight["weapon"], knight["potion"])

    knight["name"].armour_protection()
    knight["name"].apply_weapon()
    knight["name"].apply_potion_if_exist()
    print(knight["name"])
    return knight["name"]


def knight_battle(knight_1: Knight, knight_2: Knight) -> None:
    knight_1.battle(knight_2)
    knight_2.battle(knight_1)

    knight_1.check_fell()
    knight_2.check_fell()
