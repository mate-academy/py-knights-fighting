from app.modules.knight import Knight
from app.modules.knights import knights as knights_origin_dict


def battle(knights: dict) -> dict:
    # storage of all knights objects in a dictonary
    knights_dict = {}
    # parse inner knights dict. In an each iteration adds all knight features
    for knight_unit in knights.values():
        knights_dict[knight_unit["name"]] = Knight(
            knight_unit["name"],
            knight_unit["power"],
            knight_unit["hp"]
        )
        knights_dict[knight_unit["name"]].apply_armour(knight_unit["armour"])
        knights_dict[knight_unit["name"]].apply_weapon(knight_unit["weapon"])
        knights_dict[knight_unit["name"]].apply_potion(knight_unit["potion"])

    # create instance variables for better reading of code
    lancelot = Knight.knights["Lancelot"]
    arthur = Knight.knights["Arthur"]
    mordred = Knight.knights["Mordred"]
    red_knight = Knight.knights["Red Knight"]

    print(Knight.knights["Lancelot"])
    # run battles
    Knight.battle(lancelot, mordred)
    Knight.battle(red_knight, arthur)

    return {
        knight_name: knight_value.health
        for knight_name, knight_value in knights_dict.items()
    }


print(battle(knights_origin_dict))
