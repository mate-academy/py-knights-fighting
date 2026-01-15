from app.knight.knight import Knight
from app.knight.weapon import Weapon
from app.knight.armour import Armour
from app.knight.potion import Potion
from app.knight.effect import Effect


def convert_dict_to_oop(config: dict) -> list:
    result = []
    for knight, value in config.items():
        knight_obj = Knight(
            name=value["name"],
            power=value["power"],
            hp=value["hp"],
            weapon=Weapon(
                name=value["weapon"]["name"],
                power=value["weapon"]["power"]
            )
        )
        if value["potion"] is not None:
            knight_obj.potion = Potion(
                name=value["potion"]["name"],
                effect=Effect()
            )
            for arg, force in value["potion"]["effect"].items():
                knight_obj.potion.effect.__setattr__(arg, force)
        if value["armour"]:
            armour_list = []
            for armour in value["armour"]:
                armour_obj = Armour(
                    part=armour["part"],
                    protection=armour["protection"]
                )
                armour_list.append(armour_obj)
            knight_obj.armour = armour_list
        result.append(knight_obj)
    return result
