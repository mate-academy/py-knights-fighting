from app.items import Weapon, Armour, Potion
from app.warriors import Knight
from app.data import KNIGHTS


def battle(knights_config: dict) -> dict:
    knights = {}

    for warrior, config in knights_config.items():
        knight = Knight(name=config["name"],
                        power=config["power"],
                        hp=config["hp"])

        knight.weapon_up(Weapon(name=config["weapon"]["name"],
                                power=config["weapon"]["power"]))

        for armour in config["armour"]:
            knight.armour_up(Armour(part=armour["part"],
                                    protection=armour["protection"]))

        if config["potion"]:
            power = config["potion"]["effect"].get("power", 0)
            hp = config["potion"]["effect"].get("hp", 0)
            protection = config["potion"]["effect"].get("protection", 0)
            knight.use_potion(Potion(name=config["potion"]["name"],
                                     power=power,
                                     hp=hp,
                                     protection=protection))

        knights[warrior] = knight

    knights["lancelot"].strike_enemy(knights["mordred"])
    knights["mordred"].strike_enemy(knights["lancelot"])
    knights["arthur"].strike_enemy(knights["red_knight"])
    knights["red_knight"].strike_enemy(knights["arthur"])

    return {data.name: data.hp for data in knights.values()}


print(battle(KNIGHTS))
