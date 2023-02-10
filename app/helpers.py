"""
script which contains functions
that are not depend on special class or instance call
may be further organized or expanded into package module if needed
"""

from app.knight import Knight
from app.item import Item


def get_knights(config: dict) -> dict:
    """
    creates new instance of knight and looks for knight info
    calls get_item to collect all info on equipment and instantiate it
    returns dict of knights in form name: instance
    """
    knights = {}
    for knight_info in config.values():
        knight_name = knight_info["name"]
        knight_power = knight_info["power"]
        knight_hp = knight_info["hp"]
        knights[knight_name] = Knight(name=knight_name,
                                      initial_power=knight_power,
                                      initial_hp=knight_hp)
        knight_items = get_items(knight_info)
        knights[knight_name].take_items(knight_items)
    return knights


def get_items(knight_info: dict) -> list:
    """
    searches for items and istantiate necessary class object to store its info
    returns list of Item instances ready to be used by Knight instance
    may be modified to add more items to look for
    """
    item_list = list()
    if knight_info["armour"]:
        armour_list = knight_info.get("armour")
        for armourpiece in armour_list:
            item_list.append(Item(item_kind="equip",
                             name=armourpiece["part"],
                             stats={"protection": armourpiece["protection"]}))
    if knight_info["weapon"]:
        weapon = knight_info.get("weapon")
        item_list.append(Item(item_kind="equip",
                         name=weapon["name"],
                         stats={"power": weapon["power"]}))
    if knight_info["potion"]:
        potion = knight_info.get("potion")
        item_list.append(Item(item_kind="use",
                         name=potion["name"],
                         stats=potion["effect"]))
    return item_list


def fight_duel(knight1: Knight, knight2: Knight) -> None:
    """
    simple function for both sides perform their action
    may be modified into cycle if death dueling is allowed
    (in such case apropriate check should be implemented in Knight class)
    """
    knight1.get_strike(knight2.power)
    knight2.get_strike(knight1.power)
