from app.knights_pack.knights_data import Knight
from app.battle_pack.prepare_for_battle import PrepareForBattle
from app.battle_pack.knights_battle import KnightsBattle
from app.knights_pack.knights_store import KNIGHTS_DICT


def battle(knights_config: dict) -> dict:
    knights_obj = []

    for knight in knights_config.values():
        knight_prot = sum(a["protection"] for a in knight["armour"])\
            if knight["armour"] else 0
        single_knight = Knight(
            knight["name"],
            knight["hp"],
            knight["power"] + knight["weapon"]["power"],
            knight_prot,
        )

        if knight["potion"]:
            effect = knight["potion"]["effect"]
            if "hp" in effect:
                PrepareForBattle.give_armor(single_knight, effect["hp"])
            if "power" in effect:
                PrepareForBattle.give_power(single_knight, effect["power"])
            if "protection" in effect:
                PrepareForBattle.give_protection(single_knight,
                                                 effect["protection"])

        knights_obj.append(single_knight)

    KnightsBattle.battle(knights_obj[0], knights_obj[2])
    KnightsBattle.battle(knights_obj[1], knights_obj[3])

    return {k.name: k.knight_hp for k in knights_obj}


print(battle(KNIGHTS_DICT))
