from app.modules.knight import Knight
from app.modules.knights import knights as knights_origin_dict


def battle(knights: dict) -> dict:
    # storage of all knights objects in a dictonary
    knights_dict = {}
    # parse inner knights dict. In an each iteration adds all knight features
    for kn in knights.values():
        knights_dict[kn["name"]] = Knight(kn["name"], kn["power"], kn["hp"])
        knights_dict[kn["name"]].apply_armour(kn["armour"])
        knights_dict[kn["name"]].apply_weapon(kn["weapon"])
        knights_dict[kn["name"]].apply_potion(kn["potion"])

    # create instance variables for better reading of code
    lancelot = Knight.knights["Lancelot"]
    arthur = Knight.knights["Arthur"]
    mordred = Knight.knights["Mordred"]
    red_knight = Knight.knights["Red Knight"]

    print(Knight.knights["Lancelot"])
    # run battles
    Knight.battle(lancelot, mordred)
    Knight.battle(red_knight, arthur)

    return {name: val.health for name, val in knights_dict.items()}


print(battle(knights_origin_dict))
