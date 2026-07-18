from app.Knight.Knight import knight_instances


def prepare_to_battle(list_of_instances):
    equipped_knights =[]
    for knight in list_of_instances:
        for armour_pice in knight.armour:
            knight.protection += armour_pice["protection"]
        knight.power += knight.weapon["power"]
        if knight.potion:
            effect = knight.potion["effect"]
            knight.power += effect.get("power", 0)
            knight.hp += effect.get("hp", 0)
            knight.protection += effect.get("protection", 0)
        equipped_knights.append(knight)
    return equipped_knights

Equipped_knight = prepare_to_battle(knight_instances)
