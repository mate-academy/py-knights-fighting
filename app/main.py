from app.Medieval.armour import Armour
from app.Medieval.potion import Potion, Effect
from app.Medieval.weapon import Weapon
from app.Medieval.knight import Knight


def init_knights(knights_config: dict) -> dict[str, Knight]:
    dict_of_knights = {}
    for hero in knights_config.keys():
        armour_list = []
        potion_dict = knights_config[hero]["potion"]
        new_potion = None
        for armour in knights_config[hero]["armour"]:
            armour_list.append(Armour(
                part=armour["part"],
                protection=armour["protection"]
            ))
        new_weapon = Weapon(
            name=knights_config[hero]["weapon"]["name"],
            power=knights_config[hero]["weapon"]["power"])
        if potion_dict:
            new_effect = Effect(potion_dict["effect"])
            new_potion = Potion(name=potion_dict["name"], effect=new_effect)
        dict_of_knights[knights_config[hero]["name"]] = (Knight(
            name=knights_config[hero]["name"],
            power=knights_config[hero]["power"],
            hp=knights_config[hero]["hp"],
            armour=armour_list,
            weapon=new_weapon,
            potion=new_potion
        ))
    return dict_of_knights


def battle(knights_config: dict) -> dict:
    knights = init_knights(knights_config)
    lancelot = knights["Lancelot"]
    arthur = knights["Arthur"]
    mordor = knights["Mordred"]
    red_knight = knights["Red Knight"]

    lancelot_duel = Knight.duel(lancelot, mordor)
    arthur_duel = Knight.duel(arthur, red_knight)

    result_dict = {lancelot.name: lancelot_duel[0],
                   arthur.name: arthur_duel[0],
                   mordor.name: lancelot_duel[1],
                   red_knight.name: arthur_duel[1]
                   }
    return result_dict
