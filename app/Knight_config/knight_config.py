from app.Knight.Knight import dict_into_cls


def prepare_to_battle(list_of_pretendants: list) -> list:
    prepared_candidates = dict_into_cls(list_of_pretendants)
    equipped_knights = []
    for knight in prepared_candidates:
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
