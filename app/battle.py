from app.knights import Knights
from app.armour import Armour
from app.potion import Potion
from app.weapon import Weapon


def create_knight_from_dict(knight_data: dict) -> Knights:
    return Knights(
        name=knight_data["name"],
        power=knight_data["power"],
        hp=knight_data["hp"],
        armour=[
            Armour(part=armour_part["part"],
                   protection=armour_part["protection"])
            for armour_part in knight_data.get("armour", [])
        ],
        weapon=Weapon(name=knight_data["weapon"]["name"],
                      power=knight_data["weapon"]["power"]),
        potion=Potion(name=knight_data["potion"]["name"],
                      effect=knight_data["potion"]["effect"])
        if knight_data.get("potion") else None
    )


def battle(knights: dict) -> dict[str, int]:
    # Dict to objects
    knight_objects = [
        create_knight_from_dict(knights["lancelot"]),
        create_knight_from_dict(knights["mordred"]),
        create_knight_from_dict(knights["arthur"]),
        create_knight_from_dict(knights["red_knight"]),
    ]

    # Preparing for battle
    for knight in knight_objects:
        knight.prepare_for_battle()

    # Battle
    conduct_battle(knight_objects[0], knight_objects[1])
    conduct_battle(knight_objects[2], knight_objects[3])

    # Return result
    return {knight.name: knight.hp for knight in knight_objects}


def conduct_battle(knight1: Knights, knight2: Knights) -> None:
    knight1.hp -= max(0, knight2.power - knight1.protection)
    knight2.hp -= max(0, knight1.power - knight2.protection)

    knight1.hp = max(0, knight1.hp)
    knight2.hp = max(0, knight2.hp)
