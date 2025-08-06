from app.knights import Knight
from app.parser import parse_knights


def battle_preparations(knight: Knight) -> None:
    if knight.armour is not None:
        for item in knight.armour:
            knight.apply_effect(item)
    if knight.weapon is not None:
        for item in knight.weapon:
            knight.apply_effect(item)
    if knight.potion is not None:
        for item in knight.potion:
            knight.apply_effect(item)


def battle_fight(knight1: Knight, knight2: Knight) -> None:
    damage1 = max(0, knight2.power - knight1.protection)
    damage2 = max(0, knight1.power - knight2.protection)
    knight1.hp = max(0, knight1.hp - damage1)
    knight2.hp = max(0, knight2.hp - damage2)


def battle(knights_dict: dict) -> dict:
    knights = parse_knights(knights_dict)
    if len(knights) < 3:
        raise ValueError("You need four knights for the battle")
    for knight in knights:
        battle_preparations(knight)
    battle_fight(knights[0], knights[2])
    battle_fight(knights[1], knights[3])
    return {knight.name: knight.hp for knight in knights}
