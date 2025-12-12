from app.knights.knight import Armor, Weapon, Potion, Knight


def dict_to_armor(armor_dict: dict) -> Armor:
    return Armor(
        armor_dict.get("part", "unknown"),
        armor_dict.get("protection", 0)
    )


def dict_to_weapon(weapon_dict: dict) -> Weapon:
    return Weapon(
        weapon_dict.get("name", "unknown"),
        weapon_dict.get("power", 0)
    )


def dict_to_potion(potion_dict: dict) -> Potion:
    if potion_dict:
        effect = potion_dict.get("effect", {})
        return Potion(
            name=potion_dict.get("name", "Unknown"),
            power=effect.get("power", 0),
            hp=effect.get("hp", 0),
            protection=effect.get("protection", 0)
        )
    else:
        return Potion()


def dict_list_to_armor_list(armor_dict_lict: [dict]) -> list[Armor]:
    return [dict_to_armor(armor_dict) for armor_dict in armor_dict_lict]


def dict_to_knight(knight_dict: dict) -> Knight:
    armor = dict_list_to_armor_list(knight_dict.get("armour", []))
    weapon = dict_to_weapon(knight_dict.get("weapon", {}))
    potion = dict_to_potion(knight_dict.get("potion", {}))

    return Knight(
        name=knight_dict.get("name", "Unknown"),
        armor=armor,
        weapon=weapon,
        potion=potion,
        power=knight_dict.get("power", 0),
        hp=knight_dict.get("hp", 0)
    )


def dict_list_to_knight_list(knight_dict: dict) -> list[Knight]:
    return [
        dict_to_knight(knight)
        for knight in knight_dict.values()
    ]
