from app.knights.knight import Knight


def knight_init(knight: dict) -> Knight:

    instance_knight = Knight(
        knight["name"],
        knight["power"],
        knight["hp"],
        knight["armour"],
        knight["weapon"],
        knight["potion"]
    )

    instance_knight.armour_prot()
    instance_knight.weapon_apply()
    instance_knight.potion_exist()
    return instance_knight


def arena(knight_0: Knight, knight_1: Knight) -> None:
    knight_0.battle(knight_1)
    knight_1.battle(knight_0)

    knight_0.check_feel()
    knight_1.check_feel()
