from app.Medieval.armour import Armour
from app.Medieval.potion import Potion, Effect
from app.Medieval.weapon import Weapon
from app.Medieval.knight import Knight


def duel(knight_1: Knight, knight_2: Knight) -> list:
    knight_1.hp -= knight_2.power - knight_1.protection
    knight_2.hp -= knight_1.power - knight_2.protection

    if knight_1.hp <= 0:
        knight_1.hp = 0

    if knight_2.hp <= 0:
        knight_2.hp = 0

    return [knight_1.hp, knight_2.hp]


def init_knights(knights_config: dict) -> None:
    Knight.list_of_knights = []
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
            new_effect = Effect()
            new_effect.get_effect(potion_dict["effect"])
            new_potion = Potion(name=potion_dict["name"], effect=new_effect)
        Knight(
            name=knights_config[hero]["name"],
            power=knights_config[hero]["power"],
            hp=knights_config[hero]["hp"],
            armour=armour_list,
            weapon=new_weapon,
            potion=new_potion
        )


def battle(knights_config: dict) -> dict:
    init_knights(knights_config)
    knights = Knight.list_of_knights
    lancelot_duel = duel(knights[0], knights[2])
    arthur_duel = duel(knights[1], knights[3])
    result_dict = {knights[0].name: lancelot_duel[0],
                   knights[1].name: arthur_duel[0],
                   knights[2].name: lancelot_duel[1],
                   knights[3].name: arthur_duel[1]
                   }
    return result_dict
